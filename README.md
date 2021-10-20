# DiMA - Diversity Motif Analyser
![PyPI - Downloads](https://img.shields.io/pypi/dm/dima-cli)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/PU-SDS/DiMA)
![GitHub issues](https://img.shields.io/github/issues-raw/PU-SDS/DiMA)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dima-cli)
![PyPI](https://img.shields.io/pypi/v/dima-cli)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/PU-SDS/DiMA)

## Table of Contents
- [What is DiMA?](#what-is-dima)
- [Installation](#installation)
- [Basic Usage](#basic-usage)
  - [Shell Command](#shell-command)
  - [Python](#python)
  - [Results](#results)
- [Advance Usage](#advance-usage)
  - [Shell Command](#shell-command)
  - [Python](#python)
  - [Results](#results)
- [Command-Line Arguments](#command-line-arguments)
- [Module Parameters](#module-parameters)

## What is DiMA?

Protein sequence diversity is one of the major challenges in the design of diagnostic, prophylactic and therapeutic 
interventions against viruses. DiMA is a tool designed to facilitate the dissection of protein sequence diversity 
dynamics for viruses. DiMA provides a quantitative measure of sequence diversity by use of Shannon’s entropy, 
applied via a user-defined k-mer sliding window. Further, the entropy value is corrected for sample size bias by 
applying a statistical adjustment. 
Additionally, DiMA further interrogates the diversity by dissecting the entropy value at each k-mer position to various 
diversity motifs. The distinct k-mer sequences at each position are classified into the following motifs based on 
their incidence. 

  - **Index**: The predominant sequence. 
  - **Major**: The sequence with the second highest incidence after the Index.
  - **Minor**: Kmers with incidence in between major and unique motifs
  - **Unique**: Kmers which are only seen once in a particular kmer position. 
  
Moreover, the description line of the sequences in the alignment can be 
formatted for inclusion of meta-data that can be tagged to the diversity motifs. DiMA enables comparative diversity 
dynamics analysis, within and between proteins of a virus species, and proteomes of different viral species.

## Installation

`pip install dima-cli`

## Basic Usage
### Shell Command
```shell
dima-cli -i aligned_sequences.afa -o results.json
```

### Python
```python
from dima import Dima
results = Dima(sequences="aligned_sequences.afa").run()
```
### Results
```
{
   "sequence_count":203,
   "support_threshold":30,
   "low_support_count":15,
   "protein_name":"Unknown Protein",
   "kmer_length":9,
   "results":[
      {
         "position":1,
         "low_support":false,
         "entropy":0.8383740426713246,
         "support":124,
         "distinct_variants_count":4,
         "distinct_variants_incidence":3.2258062,
         "variants":[
            {
               "sequence":"MKTIIALSC",
               "count":2,
               "incidence":1.6129031,
               "motif_short":"Mi",
               "motif_long":"Minor",
               "metadata":null
            },
            {
               "sequence":"MKTIIALSH",
               "count":3,
               "incidence":2.4193547,
               "motif_short":"Mi",
               "motif_long":"Minor",
               "metadata":null
            },
            {
               "sequence":"METISLISM",
               "count":1,
               "incidence":0.80645156,
               "motif_short":"U",
               "motif_long":"Unique",
               "metadata":null
            },
            {
               "sequence":"MKNIIALSY",
               "count":13,
               "incidence":10.4838705,
               "motif_short":"Ma",
               "motif_long":"Major",
               "metadata":null
            },
            {
               "sequence":"MKTIIALSY",
               "count":105,
               "incidence":84.67742,
               "motif_short":"I",
               "motif_long":"Index",
               "metadata":null
            }
         ]
      }
   ]
}
```

## Advance Usage
### Shell Command
```shell
dima-cli -i aligned_sequences.afa -o results.json -f "accession|strain|country|date"
```

### Python
```python
from dima import Dima
results = Dima(sequences="aligned_sequences.afa", header_format="accession|strain|country|date").run()
```
### Results
```
{
  "sequence_count": 3,
  "support_threshold": 30,
  "low_support_count": 18,
  "protein_name": "Unknown Protein",
  "kmer_length": 9,
  "results": [
    {
      "position": 1,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "MSASKEIKS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            }
          }
        }
      ]
    },
    {
      "position": 2,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SASKEIKSF",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 3,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ASKEIKSFL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 4,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SKEIKSFLW",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            }
          }
        }
      ]
    },
    {
      "position": 5,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KEIKSFLWT",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            }
          }
        }
      ]
    },
    {
      "position": 6,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "EIKSFLWTQ",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 7,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "IKSFLWTQS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 8,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KSFLWTQSL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 9,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SFLWTQSLR",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 10,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "FLWTQSLRR",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 11,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LWTQSLRRE",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 12,
      "low_support": true,
      "entropy": 0.914294702419047,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "WTQSLRREL",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1979": 1,
              "2012": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            }
          }
        },
        {
          "sequence": "WTQSLRRES",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "accession": {
              "AYD75365.1": 1
            },
            "date": {
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 1
            },
            "species": {
              "Homo sapiens": 1
            }
          }
        }
      ]
    },
    {
      "position": 13,
      "low_support": true,
      "entropy": 0.9286973563836846,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "TQSLRRELS",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "2012": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1
            }
          }
        },
        {
          "sequence": "TQSLRRESS",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "strain": {
              "Sierra Leone": 1
            },
            "species": {
              "Homo sapiens": 1
            },
            "date": {
              "1980": 1
            },
            "accession": {
              "AYD75365.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 14,
      "low_support": true,
      "entropy": 1.590726304378389,
      "support": 3,
      "distinct_variants_count": 3,
      "distinct_variants_incidence": 100.0,
      "variants": [
        {
          "sequence": "QSLRRESSG",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "strain": {
              "Sierra Leone": 1
            },
            "date": {
              "1980": 1
            },
            "accession": {
              "AYD75365.1": 1
            },
            "species": {
              "Homo sapiens": 1
            }
          }
        },
        {
          "sequence": "QSLRRELSS",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "accession": {
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 1
            },
            "species": {
              "Homo sapiens": 1
            },
            "date": {
              "2012": 1
            }
          }
        },
        {
          "sequence": "QSLRRELSG",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "strain": {
              "Sierra Leone": 1
            },
            "species": {
              "Unknown": 1
            },
            "accession": {
              "AYD75325.1": 1
            },
            "date": {
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 15,
      "low_support": true,
      "entropy": 1.5836823969940967,
      "support": 3,
      "distinct_variants_count": 3,
      "distinct_variants_incidence": 100.0,
      "variants": [
        {
          "sequence": "SLRRESSGY",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "accession": {
              "AYD75365.1": 1
            },
            "species": {
              "Homo sapiens": 1
            },
            "strain": {
              "Sierra Leone": 1
            },
            "date": {
              "1980": 1
            }
          }
        },
        {
          "sequence": "SLRRELSGY",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "accession": {
              "AYD75325.1": 1
            },
            "species": {
              "Unknown": 1
            },
            "date": {
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 1
            }
          }
        },
        {
          "sequence": "SLRRELSSY",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "strain": {
              "Sierra Leone": 1
            },
            "accession": {
              "QEP52131.1": 1
            },
            "species": {
              "Homo sapiens": 1
            },
            "date": {
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 16,
      "low_support": true,
      "entropy": 1.5880632175312825,
      "support": 3,
      "distinct_variants_count": 3,
      "distinct_variants_incidence": 100.0,
      "variants": [
        {
          "sequence": "LRRESSGYC",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "accession": {
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 1
            },
            "species": {
              "Homo sapiens": 1
            },
            "date": {
              "1980": 1
            }
          }
        },
        {
          "sequence": "LRRELSSYC",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "accession": {
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 1
            },
            "species": {
              "Homo sapiens": 1
            },
            "date": {
              "2012": 1
            }
          }
        },
        {
          "sequence": "LRRELSGYC",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "strain": {
              "Sierra Leone": 1
            },
            "date": {
              "1979": 1
            },
            "accession": {
              "AYD75325.1": 1
            },
            "species": {
              "Unknown": 1
            }
          }
        }
      ]
    },
    {
      "position": 17,
      "low_support": true,
      "entropy": 1.5839045388565696,
      "support": 3,
      "distinct_variants_count": 3,
      "distinct_variants_incidence": 100.0,
      "variants": [
        {
          "sequence": "RRELSSYCS",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "species": {
              "Homo sapiens": 1
            },
            "date": {
              "2012": 1
            },
            "accession": {
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 1
            }
          }
        },
        {
          "sequence": "RRELSGYCS",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "accession": {
              "AYD75325.1": 1
            },
            "species": {
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 1
            },
            "date": {
              "1979": 1
            }
          }
        },
        {
          "sequence": "RRESSGYCS",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "species": {
              "Homo sapiens": 1
            },
            "strain": {
              "Sierra Leone": 1
            },
            "date": {
              "1980": 1
            },
            "accession": {
              "AYD75365.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 18,
      "low_support": true,
      "entropy": 1.5856788550025385,
      "support": 3,
      "distinct_variants_count": 3,
      "distinct_variants_incidence": 100.0,
      "variants": [
        {
          "sequence": "RELSGYCSN",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "accession": {
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 1
            },
            "species": {
              "Unknown": 1
            },
            "date": {
              "1979": 1
            }
          }
        },
        {
          "sequence": "RESSGYCSN",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "accession": {
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 1
            },
            "date": {
              "1980": 1
            },
            "species": {
              "Homo sapiens": 1
            }
          }
        },
        {
          "sequence": "RELSSYCSN",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "date": {
              "2012": 1
            },
            "strain": {
              "Sierra Leone": 1
            },
            "accession": {
              "QEP52131.1": 1
            },
            "species": {
              "Homo sapiens": 1
            }
          }
        }
      ]
    }
  ]
}
```

## Command-Line Arguments
| **Argument** | **Type** | **Required** | **Default**                 | **Example**                                                              | **Description**                                                                               |
|--------------|----------|--------------|-----------------------------|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| -h           | N/A      | False        | N/A                         | `dima-cli -h`                                                            | Prints a summary of all available command-line arguments.                                     |
| -n           | String   | False        | N/A (raise error)           | `dima-cli -i sequences.afa -f "accession\|strain\|country" -n "Unknown"` | Silently fix missing values in the FASTA header with given value.                             |
| -v           | N/A      | False        | N/A                         | `dima-cli -v`                                                            | Prints the version of dima-cli that is currently installed.                                   |
| -p           | String   | False        | Unknown Protein             | `dima-cli -n "Coronavirus Surface Protein" -i sequences.afa`             | The name of the protein that will appear on the results.                                      |
| -i           | String   | True         | N/A                         | `dima-cli -i sequences.afa`                                              | The path to the FASTA Multiple Sequence Alignment file.                                       |
| -o           | String   | False        | stdout (prints the results) | `dima-cli -i sequences.afa -o results,json`                              | The location where the results shall be saved.                                                |
| -l           | Integer  | False        | 9                           | `dima-cli -i sequences.afa -l 12`                                        | The length of the kmers generated.                                                            |
| -f           | String   | False        | N/A                         | `dima-cli -i sequences.afa -f "accession\|strain\|country"`              | The format of the FASTA header. Labels where each variant of a kmer position originated from. |
| -s           | Integer  | False        | 30                          | `dima-cli -i sequences.afa -l 12 -s 40`                                  | The minimum required support for each kmer position.                                          |



## Module Parameters
| **Parameter**     | **Type**        | **Required** | **Default**                | **Description**                                                                                                 |
|-------------------|-----------------|--------------|----------------------------|-----------------------------------------------------------------------------------------------------------------|
| sequences         | String/StringIO | True         | N/A                        | The path to a FASTA Multiple Sequence Alignment file (MSA), or a StringIO object containing FASTA MSA.          |
| kmer_length       | Integer         | False        | 9                          | The length of the kmers generated.                                                                              |
| header_fillna     | String          | False        | None                       | Silently fix missing values in the FASTA header with given value (only required when `header_format` is given). |
| json              | Boolean         | False        | False                      | Whether the result is a JSON string, or a Python object.                                                        |
| header_format     | String          | False        | N/A                        | The format of the FASTA header. Labels where each variant of a kmer position originated from.                   |
| support_threshold | Integer         | False        | 30                         | The minimum required support for each kmer position.                                                            |
| protein_name      | String          | False        | Unknown Protein            | The name of the protein that will appear on the results.                                                        |
| json_save_path    | String          | False        | stdout (prints to console) | The location where the results shall be saved (only required when ```json = True```).                           |
