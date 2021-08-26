extern crate pyo3;
extern crate rand;
extern crate linreg;
extern crate bio;
extern crate serde_json;
extern crate serde;
extern crate rayon;

use std::collections::{HashMap};
use pyo3::prelude::*;
use rand::seq::{SliceRandom, IteratorRandom};
use linreg::linear_regression_of;
use bio::io::fasta;
use std::fs::File;
use serde::Serialize;
use rayon::prelude::*;
use std::io::Write;
use pyo3::{PyObjectProtocol};

#[pyclass]
#[pyo3(text_signature = "(sequence_count, support_threshold, low_support, protein_name, kmer_length, results)")]
#[derive(Serialize)]
pub struct Results {
    #[pyo3(get)]
    sequence_count: usize,

    #[pyo3(get)]
    support_threshold: usize,

    #[pyo3(get)]
    low_support: bool,

    #[pyo3(get)]
    protein_name: String,

    #[pyo3(get)]
    kmer_length: usize,

    #[pyo3(get)]
    results: Vec<Position>,
}

#[pyclass]
#[pyo3(text_signature = "(position, low_support, entropy, support, distinct_variants_count, distinct_variants_incidence, variants)")]
#[derive(Serialize, Clone)]
pub struct Position {
    #[pyo3(get)]
    position: usize,

    #[pyo3(get)]
    low_support: bool,

    #[pyo3(get)]
    entropy: f64,

    #[pyo3(get)]
    support: usize,

    #[pyo3(get)]
    distinct_variants_count: usize,

    #[pyo3(get)]
    distinct_variants_incidence: f32,

    #[pyo3(get)]
    variants: Option<Vec<Variant>>,
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
    metadata: Option<HashMap<String, Vec<String>>>,
}

#[pymethods]
impl Position {
    /// This method allows one to get a particular variant from a kmer position.
    ///
    /// # Parameters:
    /// * `sort` - The sorting order (ie: asc, desc)
    ///
    /// :param sort: The sorting order (ie: asc, desc)
    /// :type sort: Literal['asc', 'desc']
    ///
    /// Example:
    /// >>> results[10].get_minors('asc')
    #[pyo3(text_signature = "(sort)")]
    fn get_minors(&self, sort: Option<String>) -> Option<Vec<Variant>> {
        let mut variant_matches = self
            .variants
            .as_ref()?
            .into_par_iter()
            .filter(|variant| variant.motif_short.as_ref().unwrap() == "Mi")
            .map(|variant| variant.to_owned())
            .collect::<Vec<Variant>>();


        variant_matches.sort_by(|a, b| return if sort.as_ref().is_none() | (sort.as_ref().unwrap() == "asc") { a.count.cmp(&b.count) } else { b.count.cmp(&a.count) });

        Some(variant_matches)
    }
}

impl Position {
    /// Returns a new Position object.
    /// This is where motif classification takes place.
    ///
    /// # Parameters:
    /// * `position` - The k-mer position we are dealing with.
    /// * `entropy` - The entropy value for this position.
    /// * `support` - How much support is present for this position (count of valid k-mers)
    /// * `variants` - All the k-mer variants seen at this k-mer position.
    pub fn new(
        position: usize,
        entropy: f64,
        support: usize,
        variants: Option<&mut Vec<Variant>>,
        low_support: bool,
    ) -> Self {
        let mut position_obj = Self {
            position,
            support,
            entropy,
            variants: None,
            distinct_variants_count: 0,
            distinct_variants_incidence: 0.0,
            low_support,
        };

        if variants.is_none() { return position_obj; }
        let variants_unwrapped = variants.unwrap();

        let mut max_incidence = variants_unwrapped
            .iter()
            .reduce(|a, b| return if a.count < b.count { b } else { a })
            .unwrap()
            .count;

        variants_unwrapped.into_iter().for_each(|variant| {
            if variant.count == max_incidence {
                if variant.count != 1 {
                    variant.motif_long = Some("Index".parse().unwrap());
                    variant.motif_short = Some("I".parse().unwrap());
                }
            }

            if variant.count == 1 {
                variant.motif_long = Some("Unique".parse().unwrap());
                variant.motif_short = Some("U".parse().unwrap());
            }
        });

        let pending_classification = &mut variants_unwrapped
            .iter_mut()
            .filter(|variant| variant.motif_long == None)
            .collect::<Vec<&mut Variant>>();

        if pending_classification.is_empty() {
            let distinct_variants_count = variants_unwrapped
                .into_par_iter()
                .filter(|variant| variant.motif_short != Some('I'.to_string()))
                .count();
            position_obj.distinct_variants_count = distinct_variants_count;
            position_obj.distinct_variants_incidence = (
                distinct_variants_count as f32 / support as f32
            ) * 100_f32;
            position_obj.variants = Some(variants_unwrapped.to_owned());

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

        let distinct_variants_count = variants_unwrapped
            .into_par_iter()
            .filter(|variant| variant.motif_short != Some('I'.to_string()))
            .count();
        position_obj.distinct_variants_count = distinct_variants_count;
        position_obj.distinct_variants_incidence = (
            distinct_variants_count as f32 / support as f32
        ) * 100_f32;
        position_obj.variants = Some(variants_unwrapped.to_owned());

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
fn transpose_kmers<T>(kmers: Vec<Vec<T>>) -> Vec<Vec<T>> {
    assert!(!kmers.is_empty());
    let len = kmers[0].len();
    let mut iters: Vec<_> = kmers.into_iter().map(|n| n.into_iter()).collect();
    (0..len)
        .map(|_| {
            iters
                .iter_mut()
                .map(|n| n.next().unwrap())
                .collect::<Vec<T>>()
        })
        .collect()
}

/// Uses the Sliding Window approach to generate k-mers of a specific length.
///
/// # Parameters:
/// * `sequence` - The sequence of amino-acids.
/// * `kmer_length` - The length of the k-mers to be generated.
/// * `illegal_chars` - Characters that are not allowed in a valid k-mer.
fn sliding_window(sequence: &String, kmer_length: &usize, illegal_chars: &Vec<char>) -> Vec<String> {
    sequence
        .chars()
        .collect::<Vec<char>>()
        .windows(*kmer_length)
        .map(|kmer_chars| {
            let iter = kmer_chars.into_iter();
            if iter.clone().any(|f| { illegal_chars.contains(f) }) { return String::from("NA"); }
            iter.collect()
        })
        .collect::<Vec<String>>()
}

/// Returns the the frequency of distinct k-mers in a provided k-mer position, as well as the
/// locations at which each distinct k-mer was observed in the list of sequences.
///
/// # Parameters:
/// * `position_kmers` - All k-mers of a specific k-mer position.
fn count_kmers(position_kmers: &Vec<String>) -> HashMap<String, (usize, Vec<usize>)> {
    let mut counts: HashMap<String, (usize, Vec<usize>)> = HashMap::new();

    position_kmers
        .into_iter()
        .enumerate()
        .for_each(|(idx, kmer)| {
            let entry = counts.entry(kmer.to_owned()).or_insert((0, vec![]));
            entry.0 += 1;
            entry.1.push(idx);
        });

    counts
}

/// Here we parse the FASTA header. We expect a header that looks like:
/// accession|species|country|year
///
/// # Parameters:
/// * `header` - The specific header we are decoding.
/// * `format` - The format of the header as provided by the user.
///
/// Returns a HashMap (dictionary) containing the components of the header.
fn parse_header(header: &String, format: &Vec<String>) -> HashMap<String, String> {
    let metadata = header.split("|").collect::<Vec<&str>>();

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
        .map(|(idx, item)| (item.to_owned(), metadata[idx].to_owned()))
        .collect::<HashMap<String, String>>()
}

/// Produces a given number of random samples from a bunch of k-mers.
///
/// # Parameters:
/// * `position_kmers` - A bunch of k-mers seen at a particular k-mer position.
/// * `sample_size` - The number of samples to be taken.
fn get_random_samples(position_kmers: &Vec<String>, sample_size: usize) -> Vec<String> {
    (0..sample_size)
        .into_par_iter()
        .map(|_| position_kmers.choose(&mut rand::thread_rng()).unwrap().to_owned())
        .collect::<Vec<String>>()
}

/// Calculate the entropy of a specific k-mer position using the Shannon's Entropy formula.
/// Adjustments are done for alignment-bias by getting the y-intercept of a entropy vs 1/N
/// linear regression,
///
/// # Parameters:
/// * `position_kmers` -  All k-mers of a specific k-mer position.
fn calculate_entropy(position_kmers: &Vec<String>) -> f64 {
    let kmer_count = position_kmers.len();

    if kmer_count == 0 { return 0.0_f64; }

    let entropies: Vec<(f64, f64)> = (1..100)
        .into_par_iter()
        .map(
            |_i| {
                let mut rng = rand::thread_rng();
                let mut iter_entropy: f64 = 0.0;
                // TODO: What if there are more than 1000 kmers?
                let samples: usize = (1..1000).choose(&mut rng).unwrap();

                let random_samples = get_random_samples(position_kmers, samples);
                let sample_counted = count_kmers(&random_samples)
                    .into_iter()
                    .map(|(_i, d)| d.0);

                sample_counted.for_each(|count| {
                    let p: f64 = count as f64 / samples as f64;
                    iter_entropy += p * p.log2();
                });

                if iter_entropy < 0_f64 { iter_entropy *= -1 as f64 };

                return (1.0 / samples as f64, iter_entropy);
            }
        ).collect::<Vec<(f64, f64)>>();

    let (_, y) = linear_regression_of(&entropies).unwrap();
    y
}

/// Uses a file buffer that progressively reads each sequence from the disk.
/// The advantage of this is that it will use as little memory as possible.
/// We will iterate over each sequence and process them on the fly to reduce the memory footprint
/// as much as possible.
///
/// # Parameters:
/// * `path` - The path to the FASTA file.
/// * `kmer_length` - The length of the k-mers that need to be generated.
/// * `header_format` - The format of the FASTA headers.
/// * `support_threshold` - Minimum support needed for a k-mer position to be considered valid.
fn get_kmers_and_headers(
    path: &String,
    kmer_length: &usize,
    header_format: Option<&Vec<String>>,
    support_threshold: usize,
) -> (Vec<Vec<String>>, Option<Vec<HashMap<String, String>>>, usize) {
    let illegal_chars: &Vec<char> = &vec!['-', 'X', 'B', 'J', 'Z', 'O', 'U'];
    let mut sequence_kmers: Vec<Vec<String>> = vec![];
    let mut headers: Vec<HashMap<String, String>> = vec![];

    let records = fasta::Reader::new(File::open(path)
        .expect("Failed to read FASTA file"))
        .records();

    let mut sequence_count: usize = 0;

    records.for_each(|r| {
        sequence_count += 1;
        let record = r.unwrap().clone();

        sequence_kmers.push(
            sliding_window(
                &String::from_utf8(Vec::from(record.seq())).unwrap(),
                &kmer_length,
                illegal_chars,
            )
        );

        if header_format.is_some() {
            headers.push(
                parse_header(&record.id().to_string(), header_format.unwrap())
            );
        }
    });

    let mut transposed_kmers = transpose_kmers(sequence_kmers);

    transposed_kmers
        .par_iter_mut()
        .for_each(|kmer_position| kmer_position.retain(|kmer| kmer != "NA"));

    (transposed_kmers, if headers.is_empty() { None } else { Some(headers) }, sequence_count)
}

/// This is one of the two main functions that are accessible from Python side.
/// It uses the get_results_obj function to generate the results, and then converts the results
/// into JSON.
///
/// This function does not return anything. If a save path is defined, it will save the JSON
/// results to this path, or else send the results to STDOUT.
///
/// # Parameters:
/// * `path` - The full path to the FASTA file.
/// * `kmer_length` - The length of k-mers to generate.
/// * `header_format` - The format of the FASTA header.
/// * `support_threshold` - Minimum support needed for a k-mer position to be considered valid.
/// * `protein_name` - The name of the protein being analysed.
/// * `save_path` - The file path to save the JSON results to.
///
/// :param path: The full path to the FASTA file.
/// :param kmer_length: The length of k-mers to generate (default: 9).
/// :param header_format: The format of the FASTA header.
/// :param support_threshold: Minimum support needed for a k-mer position to be considered valid (default: 30).
/// :param protein_name: The name of the protein being analysed (default: Unknown Protein).
/// :param save_path: The file path to save the JSON results to.
///
/// :type path: str
/// :type kmer_length: int
/// :type header_format: Optional[List[str]]
/// :type support_threshold: int
/// :type protein_name: str
/// :type save_path: Optional[str]
///
/// :return: None
#[pyfunction]
#[pyo3(text_signature = "(path, kmer_length, header_format, support_threshold, protein_name, save_path)")]
pub fn get_results_json(
    _py: Python,
    path: String,
    kmer_length: usize,
    header_format: Option<Vec<String>>,
    support_threshold: usize,
    protein_name: String,
    save_path: Option<String>,
) {
    let json_results = serde_json::to_string_pretty(&get_results_objs(
        _py,
        path,
        kmer_length,
        header_format,
        support_threshold,
        protein_name,
    )
    ).unwrap();

    if save_path.is_some() {
        let mut f = File::create(
            save_path.unwrap()
        ).expect("Unable to create JSON file on disk.");

        f.write_all(json_results.as_bytes())
            .expect("Unable to write JSON to the created file.");

        return;
    }

    println!("{}", json_results);
}

/// This is one of the two main functions that are accessible from Python side.
///
/// # Parameters:
/// * `path` - The full path to the FASTA file.
/// * `kmer_length` - The length of k-mers to generate.
/// * `header_format` - The format of the FASTA header.
/// * `support_threshold` - Minimum support needed for a k-mer position to be considered valid.
/// * `protein_name` - The name of the protein being analysed.
///
/// :param path: The full path to the FASTA file.
/// :param kmer_length: The length of k-mers to generate (default: 9).
/// :param header_format: The format of the FASTA header.
/// :param support_threshold: Minimum support needed for a k-mer position to be considered valid (default: 30).
/// :param protein_name: The name of the protein being analysed (default: Unknown Protein).
///
/// :type path: str
/// :type kmer_length: int
/// :type header_format: Optional[List[str]]
/// :type support_threshold: int
/// :type protein_name: str
///
/// :return: A Results object
#[pyfunction]
#[pyo3(text_signature = "(path, kmer_length, header_format, support_threshold, protein_name, save_path)")]
pub fn get_results_objs(
    _py: Python,
    path: String,
    kmer_length: usize,
    header_format: Option<Vec<String>>,
    support_threshold: usize,
    protein_name: String,
) -> Results {
    let (kmers, headers, sequence_count) = get_kmers_and_headers(
        &path,
        &kmer_length,
        Option::from(&header_format),
        support_threshold,
    );


    let position_entropies = kmers
        .par_iter()
        .map(|position_kmers| calculate_entropy(position_kmers))
        .collect::<Vec<f64>>();

    let positions = kmers
        .iter()
        .map(|position_kmers| count_kmers(position_kmers))
        .enumerate()
        .map(|(idx, position_count)| {
            let mut variants = position_count.par_iter().map(|(sequence, count_data)| {
                let mut variant = Variant {
                    sequence: sequence.to_owned(),
                    count: count_data.0,
                    incidence: ((count_data.0 as f32 / kmers[idx].len() as f32) * 100_f32),
                    metadata: None,
                    motif_short: None,
                    motif_long: None,
                };

                let mut metadata: HashMap<String, Vec<String>> = HashMap::new();

                if header_format.is_some() {
                    count_data.1.iter().for_each(|idx| {
                        header_format.as_ref().unwrap().iter().for_each(|item| {
                            let entry = metadata.entry(item.to_owned()).or_insert(
                                vec![]
                            );
                            entry.push(
                                headers.as_ref().unwrap()[*idx].get(item).unwrap().to_owned()
                            );
                        });
                    });

                    variant.metadata = Some(metadata);
                } else {
                    variant.metadata = None;
                };

                variant
            }).collect::<Vec<Variant>>();

            let support = kmers[idx].len();

            return Position::new(
                idx + 1,
                position_entropies[idx],
                support,
                if variants.is_empty() { None } else { Some(&mut variants) },
                if support >= support_threshold { false } else { true },
            );
        }).collect::<Vec<Position>>();

    Results {
        support_threshold,
        kmer_length,
        sequence_count,
        low_support: if sequence_count >= support_threshold { false } else { true },
        protein_name,
        results: positions,
    }
}

/// This is the C extensions module of DiMA. Most of the heavy-lifting of DiMA is done by methods
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
    m.add_function(wrap_pyfunction!(get_results_json, m)?)?;
    m.add_class::<Position>()?;
    m.add_class::<Variant>()?;
    m.add_class::<Results>()?;
    Ok(())
}
