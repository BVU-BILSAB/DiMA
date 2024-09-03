extern crate bio;
extern crate linreg;
extern crate pyo3;
extern crate rand;
extern crate rayon;
extern crate serde;
extern crate serde_json;
extern crate core;
extern crate str_overlap;
extern crate statrs;

use bio::io::fasta;
use linreg::linear_regression_of;
use pyo3::prelude::*;
use pyo3::PyObjectProtocol;
use pyo3::exceptions::{PyFileNotFoundError, PyIOError};
use rand::seq::{SliceRandom};
use rayon::prelude::*;
use serde::Serialize;
use std::collections::HashMap;
use std::fs::File;
use std::io::Write;
use statrs::statistics::Statistics;
use str_overlap::*;


fn excel_pos_col_titles() -> Vec<&'static str> {
    vec!["Position", "Diversity Motifs", "Low Support",
         "Entropy", "Support", "Distinct Variants",
         "Distinct Variants Incidence", "Total Variants Incidence"]
}

fn excel_variants_col_titles() -> Vec<&'static str> {
    vec!["Sequence", "Count", "Incidence", "Motif"]
}


#[pyclass]
#[pyo3(
text_signature = "(position, entropy)"
)]
#[derive(Serialize, Clone)]
pub struct HighestEntropy {
    #[pyo3(get)]
    position: usize,

    #[pyo3(get)]
    entropy: f64,
}

fn get_highest_number_and_index(numbers: &[f64]) -> HighestEntropy {
    let highest_position = numbers
        .into_iter()
        .enumerate()
        .reduce(|acc, item| {
            if acc.1 > item.1 { acc } else { item }
        })
        .unwrap();

    HighestEntropy { position: highest_position.0, entropy: *highest_position.1 }
}

#[pyclass]
#[pyo3(
text_signature = "(sequence_count, support_threshold, low_support_count, protein_name, kmer_length, results)"
)]
#[derive(Serialize)]
pub struct Results {
    #[pyo3(get)]
    sequence_count: usize,

    #[pyo3(get)]
    support_threshold: usize,

    #[pyo3(get)]
    low_support_count: usize,

    #[pyo3(get)]
    query_name: String,

    #[pyo3(get)]
    kmer_length: usize,

    #[pyo3(get)]
    highest_entropy: HighestEntropy,

    #[pyo3(get)]
    average_entropy: f64,

    #[pyo3(get)]
    results: Vec<Position>,
}

#[pyclass]
#[pyo3(
text_signature = "(position, low_support, entropy, support, distinct_variants_count, distinct_variants_incidence, variants)"
)]
#[derive(Serialize, Clone)]
pub struct Position {
    #[pyo3(get)]
    position: usize,

    #[pyo3(get)]
    low_support: Option<String>,

    #[pyo3(get)]
    entropy: f64,

    #[pyo3(get)]
    support: usize,

    #[pyo3(get)]
    distinct_variants_count: usize,

    #[pyo3(get)]
    distinct_variants_incidence: f32,

    #[pyo3(get)]
    total_variants_incidence: f32,

    #[pyo3(get)]
    diversity_motifs: Option<Vec<Variant>>,
}

#[pyclass]
#[pyo3(text_signature = "(sequence, count, incidence, motif_short, motif_long, metadata)")]
#[derive(Clone, Serialize)]
pub struct Variant {
    #[pyo3(get)]
    sequence: String,

    #[pyo3(get)]
    count: usize,

    #[pyo3(get)]
    incidence: f32,

    #[pyo3(get)]
    motif_short: Option<String>,

    #[pyo3(get)]
    motif_long: Option<String>,

    #[pyo3(get)]
    metadata: Option<HashMap<String, HashMap<String, usize>>>,
}

fn save_file(content: &str, path: &str) -> Result<(), PyErr> {
    if let Ok(mut f) = File::create(path) {
        if f.write_all(content.as_bytes()).is_ok() {
            Ok(())
        } else {
            Err(PyIOError::new_err("Cannot write to file."))
        }
    } else {
        Err(PyFileNotFoundError::new_err("Unable to create on disk."))
    }
}

#[pymethods]
impl Results {
    #[pyo3(text_signature = "(path, threshold)")]
    fn get_hcs(&self, path: Option<String>, threshold: Option<f32>) -> Result<Vec<String>, PyErr> {
        let hcs = self
            .results
            .iter()
            .flat_map(|position| position.diversity_motifs.as_ref())
            .flatten()
            .filter(|variant| variant.motif_short.as_ref().unwrap() == "I")
            .filter(|variant| if threshold.is_none() { true } else { variant.incidence >= threshold.unwrap() })
            .fold("".to_string(), |acc, variant| {
                let sequence = variant.sequence.as_str();
                let overlap = acc.overlap_end(sequence);
                let mut new_acc = acc.to_string();

                return if overlap.is_empty() {
                    if acc.is_empty() {
                        return sequence.to_string();
                    }

                    new_acc.push(',');
                    new_acc.push_str(sequence);

                    new_acc
                } else {
                    if let Some(last_residue) = sequence.chars().last() {
                        new_acc.push(last_residue);

                        new_acc
                    } else {
                        sequence.to_string()
                    }
                };
            })
            .split(",")
            .map(|hcs| hcs.to_string())
            .collect::<Vec<String>>();

        if let Some(save_path) = path {
            let json_results = serde_json::to_string_pretty(&hcs).unwrap();

            match save_file(json_results.as_str(), save_path.as_str()) {
                Ok(_) => {
                    Ok(hcs)
                }
                Err(error) => {
                    Err(error)
                }
            }
        } else {
            Ok(hcs)
        }
    }
    /// This method lets one convert the entire results object into JSON.
    ///
    /// # Parameters:
    /// * `path` - The path to save the JSON file.
    ///
    /// :param path: The path to save the JSON file.
    /// :type path: Optional[str]
    ///
    /// :return: A string containing the json, or "true" when successfully saved.
    #[pyo3(text_signature = "(path)")]
    fn to_json(&self, path: Option<String>) -> PyResult<String> {
        let json_results = serde_json::to_string_pretty(&self).unwrap();

        if let Some(save_path) = path {
            match save_file(json_results.as_str(), save_path.as_str()) {
                Ok(_) => {
                    Ok(json_results)
                }
                Err(error) => {
                    Err(error)
                }
            }
        } else {
            Ok(json_results)
        }
    }
}

#[pymethods]
impl Position {
    /// This method allows one to get a sorted list of Minor variants from a kmer position.
    ///
    /// # Parameters:
    /// * `sort` - The sorting order (ie: asc, desc)
    ///
    /// :param sort: The sorting order (ie: asc, desc)
    /// :type sort: Optional[Literal['asc', 'desc']]
    ///
    /// Example:
    /// >>> results[10].get_minors('asc')
    /// >>> results[10].get_minors() # defaults to ascending order
    #[pyo3(text_signature = "(sort)")]
    fn get_minors(&self, sort: Option<String>) -> Option<Vec<Variant>> {
        let mut variant_matches = self
            .diversity_motifs
            .as_ref()?
            .iter()
            .filter(|variant| variant.motif_short.as_ref().unwrap() == "Mi")
            .map(|variant| variant.to_owned())
            .collect::<Vec<Variant>>();

        variant_matches
            .par_sort_by(|a, b| {
                if sort.as_ref().is_none() {
                    a.count.cmp(&b.count)
                } else if sort.as_ref().unwrap() == "asc" {
                    a.count.cmp(&b.count)
                } else if sort.as_ref().unwrap() == "desc" {
                    b.count.cmp(&a.count)
                } else {
                    panic!("{}", "\n\nUnrecognized sorting option. Should either be empty, or one of:\n\t- asc\n\t- desc\n\n")
                }
            });

        Some(variant_matches)
    }
}

fn get_distinct_variant_counts(variants: &[Variant]) -> (usize, usize) {
    let distinct_variants = variants
        .into_iter()
        .filter(|variant| variant.motif_short != Some('I'.to_string()));

    let mut count = 0;
    let mut total = 0;

    for variant in distinct_variants {
        total += variant.count;
        count += 1;
    }

    (count, total)
}

fn set_pos_obj_data(position_obj: &mut Position, variants: &[Variant], support: &usize) {
    let (distinct_variant_count, distinct_variants_total) = get_distinct_variant_counts(variants);
    let index_count = support - distinct_variants_total;
    let distinct_variants_incidence = (distinct_variant_count as f32 / (*support - index_count) as f32) * 100_f32;
    let total_variance = (distinct_variants_total as f32 / *support as f32) * 100_f32;

    position_obj.distinct_variants_count = distinct_variant_count;
    position_obj.distinct_variants_incidence = if distinct_variants_incidence.is_nan() { 0.0 } else { distinct_variants_incidence };
    position_obj.diversity_motifs = Some(variants.to_vec());
    position_obj.total_variants_incidence = if total_variance.is_nan() { 0.0 } else { total_variance };
}

impl Position {
    pub fn new(
        position: usize,
        entropy: f64,
        support: usize,
        variants: Option<&mut Vec<Variant>>,
        low_support: Option<String>,
    ) -> Self {
        let mut position_obj = Self {
            position,
            support,
            entropy,
            diversity_motifs: None,
            distinct_variants_count: 0,
            total_variants_incidence: 0.0,
            distinct_variants_incidence: 0.0,
            low_support,
        };

        if variants.is_none() {
            return position_obj;
        }

        let variants_unwrapped = variants.unwrap();

        let mut max_incidence = variants_unwrapped
            .iter()
            .reduce(|a, b| return if a.count < b.count { b } else { a })
            .unwrap()
            .count;

        variants_unwrapped.into_iter().for_each(|variant| {
            if variant.count == max_incidence {
                if variant.count != 1 {
                    variant.motif_long = Some("Index".to_owned());
                    variant.motif_short = Some("I".to_string());
                }
            }

            if variant.count == 1 {
                variant.motif_long = Some("Unique".to_owned());
                variant.motif_short = Some("U".to_string());
            }
        });

        let pending_classification = &mut variants_unwrapped
            .iter_mut()
            .filter(|variant| variant.motif_long == None)
            .collect::<Vec<&mut Variant>>();

        if pending_classification.is_empty() {
            set_pos_obj_data(&mut position_obj, variants_unwrapped.as_slice(), &support);
            return position_obj;
        }

        max_incidence = pending_classification
            .into_iter()
            .reduce(|a, b| return if a.count < b.count { b } else { a })
            .unwrap()
            .count;

        pending_classification.iter_mut().for_each(|variant| {
            if variant.count == max_incidence {
                variant.motif_long = Some("Major".parse().unwrap());
                variant.motif_short = Some("Ma".parse().unwrap());
            } else {
                variant.motif_long = Some("Minor".parse().unwrap());
                variant.motif_short = Some("Mi".parse().unwrap());
            }
        });

        set_pos_obj_data(&mut position_obj, variants_unwrapped.as_slice(), &support);
        position_obj
    }
}

#[pyproto]
impl PyObjectProtocol for Position {
    fn __str__(&self) -> String {
        serde_json::to_string_pretty(self).unwrap()
    }

    fn __repr__(&self) -> String {
        serde_json::to_string_pretty(self).unwrap()
    }
}

#[pyproto]
impl PyObjectProtocol for Variant {
    fn __str__(&self) -> String {
        serde_json::to_string_pretty(self).unwrap()
    }

    fn __repr__(&self) -> String {
        serde_json::to_string_pretty(self).unwrap()
    }
}

#[pyproto]
impl PyObjectProtocol for Results {
    fn __str__(&self) -> String {
        serde_json::to_string_pretty(self).unwrap()
    }

    fn __repr__(&self) -> String {
        serde_json::to_string_pretty(self).unwrap()
    }
}

/// Transposes the k-mers of each provided FASTA sequence to k-mers of each k-mer position.
///
/// # Explanation:
///
/// Sequence 1: ['ABCD', 'EFGH']
///
/// Sequence 2: ['KLMN', 'OPQR]
///
/// Result: [ ['ABCD', 'EFGH'], ['EFGH', 'OPQR'] ]
///
/// # Parameters
/// * `kmers` - A vector containing the k-mers for each user-given sequence.
fn transpose_kmers(kmers: &Vec<&Vec<String>>) -> Vec<Vec<String>> {
    assert!(!kmers.is_empty());

    let len = kmers[0].len();
    let mut iters: Vec<_> = kmers.into_iter().map(|n| n.into_iter()).collect();

    (0..len)
        .map(|_| {
            iters
                .iter_mut()
                .map(|n| n.next().unwrap().to_owned())
                .collect::<Vec<String>>()
        })
        .collect()
}

/// Uses the Sliding Window approach to generate k-mers of a specific length.
///
/// # Parameters:
/// * `sequence` - The sequence of amino-acids.
/// * `kmer_length` - The length of the k-mers to be generated.
/// * `illegal_chars` - Characters that are not allowed in a valid k-mer.
fn sliding_window(
    sequence: &String,
    kmer_length: &usize,
    illegal_chars: &Vec<char>,
) -> Vec<String> {
    sequence
        .chars()
        .collect::<Vec<char>>()
        .windows(*kmer_length)
        .map(|kmer_chars| {
            let iter = kmer_chars.into_iter();
            if iter.clone().any(|f| illegal_chars.contains(f)) {
                return String::from("NA");
            }
            iter.collect()
        })
        .collect::<Vec<String>>()
}

fn count_kmers<'a>(kmers: &'a [Box<str>]) -> HashMap<&'a str, (usize, Vec<usize>)> {
    let mut counts: HashMap<&'a str, (usize, Vec<usize>)> = HashMap::new();

    kmers
        .iter()
        .enumerate()
        .for_each(|(idx, kmer)| {
            let entry = counts.entry(kmer).or_insert((0, vec![]));
            entry.0 += 1;
            entry.1.push(idx);
        });

    counts
}

fn parse_header(
    header: &String,
    format: &Vec<String>,
    fill_na: &String,
) -> HashMap<String, String> {
    let metadata = header
        .split("|")
        .map(|component| {
            return if !component.is_empty() {
                component.trim()
            } else {
                if !fill_na.is_empty() {
                    return fill_na.as_str();
                }
                component
            };
        })
        .collect::<Vec<&str>>();

    assert_eq!(
        metadata.iter().filter(|item| item.len() == 0).count(),
        0,
        "\n\nThe FASTA header looks invalid:\n\tFormat: {}\n\tHeader: {}\n\n",
        format.join("|"),
        header
    );

    assert_eq!(
        metadata.len(),
        format.len(),
        "\n\nThe header format provided does not match the header:\n\tFormat: {}\n\tHeader: {}\n\n",
        format.join("|"),
        header
    );

    format
        .iter()
        .enumerate()
        .map(|(idx, item)| (item.to_string(), metadata[idx].to_owned()))
        .collect::<HashMap<String, String>>()
}

fn get_random_samples<'a>(kmers: &[Box<str>], sample_size: &usize) -> Vec<Box<str>> {
    (0..*sample_size)
        .into_par_iter()
        .map_init(|| rand::thread_rng(), |mut rng, _| kmers
            .choose(&mut rng)
            .unwrap()
            .to_string()
            .into_boxed_str())
        .collect::<Vec<Box<str>>>()
}

fn shannons_entropy(kmers: &[Box<str>]) -> f64 {
    let kmer_count = kmers.len();
    let mut entropy = count_kmers(kmers)
        .into_iter()
        .map(|(_i, d)| d.0)
        .map(|count| {
            let p: f64 = count as f64 / kmer_count as f64;
            p * p.log2()
        })
        .sum::<f64>();

    if entropy == 0_f64 {
        return entropy;
    }

    entropy *= -1_f64;
    entropy
}


fn calculate_entropy(kmers: &[Box<str>], support_threshold: &usize) -> f64 {
    // Get the number of kmers at this position
    let kmer_count = kmers.len();

    // If the kmer count is 0 or 1, we know the entropy is 0
    if kmer_count <= 1 {
        return 0.0_f64;
    }

    // Calculate the entropy for all kmers WITHOUT resampling because we need that in both cases
    // (ie: if kmers <= threshold OR if > threshold (because 100% of the dataset will not be
    // resampled)
    let all_kmers_entropy = shannons_entropy(kmers);

    // If the kmer count is less than threshold we just return the uncorrected (un-resampled) entropy
    // value
    // This should be considered LS
    if &kmer_count < support_threshold {
        return all_kmers_entropy;
    }

    // Below this point we know that we have ample amount of kmers
    // Figure out the percentage at which we reached threshold
    let percentage_cutoff = ((*support_threshold as f64 / kmer_count as f64) * 100_f64)
        .ceil() as usize;

    // This too should be called low support too
    // For now we have NS, LS, ELS
    if percentage_cutoff == 100 {
        return all_kmers_entropy;
    }

    // Go through all the way from the percentage cutoff until 99%.
    // We ignore everything below the cutoff because we have more than enough kmers to resample
    // and we do not need to skew the regression with unreliable data
    // We stop at 99% because at 100% we do not do resampling and all kmers are used which we
    // calculated above
    let mut entropy_values: Vec<(f64, f64)> = (percentage_cutoff..99)
        .into_iter()
        .map(|percentage| {
            // Figure out the number of samples that this % represents
            let samples = (percentage * kmer_count) / 100;

            // Get the actual random samples
            let random_samples = get_random_samples(kmers, &samples);

            // Calculate the entropy
            let entropy = shannons_entropy(random_samples.as_slice());

            // Return value to the vector along with alignment bias adjustment (ie: 1/n)
            (1.0 / samples as f64, entropy)
        }).collect();

    // One of the data points has to be 100% of the k-mers WITHOUT random sampling
    entropy_values.push((1.0 / kmer_count as f64, all_kmers_entropy));

    let (_, y) = linear_regression_of(&entropy_values).unwrap();

    if y < 0_f64 {
        return all_kmers_entropy;
    }

    y
}

fn get_kmers_and_headers(
    path: &String,
    kmer_length: &usize,
    header_format: Option<&Vec<String>>,
    header_fillna: Option<&String>,
    alphabet: Option<&String>,
) -> (
    Vec<Vec<String>>,
    Option<Vec<Option<HashMap<String, String>>>>,
    usize,
) {
    let protein_ambiguous_chars = vec!['-', 'X', 'B', 'J', 'Z', 'O', 'U'];
    let nucleotide_ambiguous_chars = vec!['-', 'R', 'Y', 'K', 'M', 'S', 'W', 'B', 'D', 'H', 'V', 'N'];

    let illegal_chars = if let Some(residue_alphabet) = alphabet {
        if residue_alphabet == "protein" {
            protein_ambiguous_chars
        } else {
            nucleotide_ambiguous_chars
        }
    } else {
        protein_ambiguous_chars
    };

    let kmers_and_headers =
        fasta::Reader::new(File::open(path).expect("Failed to read FASTA file"))
            .records()
            .map(|record| {
                let record_unwrapped = record.as_ref().unwrap();

                let kmers = sliding_window(
                    &String::from_utf8(Vec::from(record_unwrapped.seq())).unwrap(),
                    &kmer_length,
                    &illegal_chars,
                );

                let mut headers: Option<HashMap<String, String>> = None;

                if let Some(headers_components) = header_format {
                    let fixed_header: String;

                    if let Some(desc) = record_unwrapped.desc() {
                        fixed_header = [record_unwrapped.id(), desc].join(" ");
                    } else {
                        fixed_header = record_unwrapped.id().to_string();
                    }

                    if let Some(fill_na) = header_fillna {
                        headers = Some(parse_header(&fixed_header, headers_components, fill_na));
                    } else {
                        headers = Some(parse_header(
                            &fixed_header,
                            headers_components,
                            &"Unknown".to_string(),
                        ));
                    }
                }

                return (kmers, headers);
            })
            .collect::<Vec<(Vec<String>, Option<HashMap<String, String>>)>>();

    let kmer_iters = &kmers_and_headers
        .iter()
        .map(|record| &record.0)
        .collect::<Vec<&Vec<String>>>();

    let mut transposed_kmers = transpose_kmers(kmer_iters);

    transposed_kmers
        .par_iter_mut()
        .for_each(|kmer_position| kmer_position.retain(|kmer| kmer != "NA"));

    let headers: Option<Vec<Option<HashMap<String, String>>>> = if header_format.is_none() {
        None
    } else {
        Some(
            kmers_and_headers
                .iter()
                .map(|record| record.1.to_owned())
                .collect::<Vec<Option<HashMap<String, String>>>>(),
        )
    };

    (transposed_kmers, headers, kmers_and_headers.len())
}

/// This is one of the two main functions that are accessible from Python side.
///
/// # Parameters:
/// * `path` - The full path to the FASTA file.
/// * `kmer_length` - The length of k-mers to generate.
/// * `header_format` - The format of the FASTA header.
/// * `alphabet` - The alphabet of the sequences (ie: protein/nucleotide, default: protein)
/// * `support_threshold` - Minimum support needed for a k-mer position to be considered valid.
/// * `query_name` - The name of the sample being analysed.
/// * `header_fillna` - If there are empty items in the FASTA header (when header_format != None), replace with this value.
///
/// :param path: The full path to the FASTA file.
/// :param kmer_length: The length of k-mers to generate (default: 9).
/// :param header_format: The format of the FASTA header.
/// :param alphabet: The alphabet of the sequences (ie: protein/nucleotide, default: protein)
/// :param support_threshold: Minimum support needed for a k-mer position to be considered valid (default: 30).
/// :param query_name: The name of the sample being analysed (default: Unknown Protein).
/// :param header_fillna: If there are empty items in the FASTA header (when header_format != None), replace with this value.
///
/// :type path: str
/// :type kmer_length: int
/// :type header_format: Optional[List[str]]
/// :type alphabet: Optional[Literal["protein", "nucleotide"]]
/// :type support_threshold: int
/// :type query_name: str
/// :type header_fillna: Optional[str]
///
/// :return: A Results object
#[pyfunction]
#[pyo3(
text_signature = "(path, kmer_length, header_format, alphabet, support_threshold, query_name, header_fillna)"
)]
pub fn get_results_objs(
    _py: Python,
    path: String,
    kmer_length: usize,
    header_format: Option<Vec<String>>,
    alphabet: Option<String>,
    support_threshold: usize,
    query_name: String,
    header_fillna: Option<String>,
) -> Results {
    let (kmers, headers, sequence_count) = get_kmers_and_headers(
        &path,
        &kmer_length,
        header_format.as_ref(),
        header_fillna.as_ref(),
        alphabet.as_ref(),
    );

    let position_slices = kmers
        .into_par_iter()
        .map(|position_kmers| position_kmers
            .into_iter()
            .map(|item| item.into_boxed_str())
            .collect::<Vec<Box<str>>>())
        .collect::<Vec<Vec<Box<str>>>>();

    let position_entropies = position_slices
        .par_iter()
        .map(|position_kmers| calculate_entropy(position_kmers, &support_threshold))
        .collect::<Vec<f64>>();

    let positions: Vec<Position> = position_slices
        .par_iter()
        .map(|position_kmers| count_kmers(position_kmers))
        .enumerate()
        .map(|(idx, position_count)| {
            let mut variants = position_count
                .par_iter()
                .map(|(sequence, count_data)| {
                    let mut variant = Variant {
                        sequence: sequence.to_string(),
                        count: count_data.0,
                        incidence: ((count_data.0 as f32 / position_slices[idx].len() as f32) * 100_f32),
                        metadata: None,
                        motif_short: None,
                        motif_long: None,
                    };

                    let mut metadata: HashMap<String, HashMap<String, usize>> = HashMap::new();

                    if let Some(header_components) = &header_format {
                        count_data.1.iter().for_each(|idx| {
                            header_components.iter().for_each(|item| {
                                let metadata_entry_hashmap =
                                    metadata.entry(item.to_string()).or_insert(HashMap::new());

                                let metadata_entry = headers.as_ref().unwrap()[*idx]
                                    .as_ref()
                                    .unwrap()
                                    .get(item)
                                    .unwrap()
                                    .to_owned();

                                metadata_entry_hashmap
                                    .entry(metadata_entry)
                                    .and_modify(|count| *count += 1)
                                    .or_insert(1);
                            });
                        });

                        variant.metadata = Some(metadata);
                    } else {
                        variant.metadata = None;
                    }

                    variant
                })
                .collect::<Vec<Variant>>();

            let support = position_slices[idx].len();

            return Position::new(
                idx + 1,
                position_entropies[idx],
                support,
                if variants.is_empty() {
                    None
                } else {
                    Some(&mut variants)
                },
                if support == 0 {
                    Some("NS".to_owned())
                } else if support < support_threshold {
                    Some("LS".to_owned())
                } else if support == support_threshold {
                    Some("ELS".to_owned())
                } else {
                    None
                },
            );
        })
        .collect::<Vec<Position>>();

    Results {
        support_threshold,
        kmer_length,
        sequence_count,
        highest_entropy: get_highest_number_and_index(position_entropies.as_slice()),
        average_entropy: position_entropies.mean(),
        low_support_count: positions
            .iter()
            .filter(|position| position.low_support.is_some())
            .count(),
        query_name,
        results: positions,
    }
}

/// This is the Rust extension module of DiMA. Most of the heavy-lifting of DiMA is done by methods
/// defined in this module.
///
/// There are two methods defined in this module:
///
/// - get_results_json
/// - get_results_objs
///
/// Three classes:
///
/// - Position
/// - Variant
/// - Results
///
/// Author: Shan Tharanga <stwm2@student.london.ac.uk>
/// ♥
#[pymodule]
fn dima(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get_results_objs, m)?)?;
    m.add_class::<Position>()?;
    m.add_class::<Variant>()?;
    m.add_class::<Results>()?;
    Ok(())
}