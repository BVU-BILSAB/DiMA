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
  "sequence_count": 3,
  "support_threshold": 30,
  "low_support_count": 567,
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
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
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
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
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
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
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
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
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
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
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
            "strain": {
              "Sierra Leone": 3
            },
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
              "2012": 1,
              "1979": 1,
              "1980": 1
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
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "1979": 1,
              "2012": 1,
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
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
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
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "strain": {
              "Sierra Leone": 3
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
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 12,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "WTQSLRREL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
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
      "position": 13,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TQSLRRELS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
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
      "position": 14,
      "low_support": true,
      "entropy": 0.9122419462231194,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
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
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "1980": 1,
              "1979": 1
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            }
          }
        }
      ]
    },
    {
      "position": 15,
      "low_support": true,
      "entropy": 0.9212028513851959,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "SLRRELSGY",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "date": {
              "1979": 1,
              "1980": 1
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
            "species": {
              "Homo sapiens": 1
            },
            "date": {
              "2012": 1
            },
            "accession": {
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 16,
      "low_support": true,
      "entropy": 0.9152708267033046,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "LRRELSGYC",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "date": {
              "1980": 1,
              "1979": 1
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
        }
      ]
    },
    {
      "position": 17,
      "low_support": true,
      "entropy": 0.9131041399832825,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "RRELSSYCS",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "date": {
              "2012": 1
            },
            "species": {
              "Homo sapiens": 1
            },
            "strain": {
              "Sierra Leone": 1
            },
            "accession": {
              "QEP52131.1": 1
            }
          }
        },
        {
          "sequence": "RRELSGYCS",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 2
            }
          }
        }
      ]
    },
    {
      "position": 18,
      "low_support": true,
      "entropy": 0.916093016569408,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
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
            "species": {
              "Homo sapiens": 1
            },
            "accession": {
              "QEP52131.1": 1
            }
          }
        },
        {
          "sequence": "RELSGYCSN",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "date": {
              "1980": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 2
            }
          }
        }
      ]
    },
    {
      "position": 19,
      "low_support": true,
      "entropy": 0.9179305226904259,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "ELSSYCSNI",
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
        },
        {
          "sequence": "ELSGYCSNI",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "date": {
              "1979": 1,
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 2
            }
          }
        }
      ]
    },
    {
      "position": 20,
      "low_support": true,
      "entropy": 0.9184633247379974,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "LSGYCSNIK",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "date": {
              "1979": 1,
              "1980": 1
            }
          }
        },
        {
          "sequence": "LSSYCSNIK",
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
        }
      ]
    },
    {
      "position": 21,
      "low_support": true,
      "entropy": 0.9226756127891819,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "SSYCSNIKL",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "strain": {
              "Sierra Leone": 1
            },
            "date": {
              "2012": 1
            },
            "species": {
              "Homo sapiens": 1
            },
            "accession": {
              "QEP52131.1": 1
            }
          }
        },
        {
          "sequence": "SGYCSNIKL",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 2
            },
            "date": {
              "1979": 1,
              "1980": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            }
          }
        }
      ]
    },
    {
      "position": 22,
      "low_support": true,
      "entropy": 0.930160418628312,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "GYCSNIKLQ",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 2
            },
            "date": {
              "1980": 1,
              "1979": 1
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            }
          }
        },
        {
          "sequence": "SYCSNIKLQ",
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
        }
      ]
    },
    {
      "position": 23,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "YCSNIKLQV",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 24,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "CSNIKLQVV",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 25,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SNIKLQVVK",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 26,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NIKLQVVKD",
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
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 27,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "IKLQVVKDA",
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
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 28,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KLQVVKDAQ",
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
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 29,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LQVVKDAQA",
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
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 30,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QVVKDAQAL",
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
              "QEP52131.1": 1,
              "AYD75325.1": 1,
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
      "position": 31,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VVKDAQALL",
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
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
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
      "position": 32,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VKDAQALLH",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
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
      "position": 33,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KDAQALLHG",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
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
      "position": 34,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DAQALLHGL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 35,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AQALLHGLD",
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
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 36,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QALLHGLDF",
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
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 37,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ALLHGLDFS",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 38,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LLHGLDFSE",
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
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 39,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LHGLDFSEV",
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
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 40,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "HGLDFSEVS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
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
      "position": 41,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GLDFSEVSN",
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
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
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
      "position": 42,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LDFSEVSNV",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
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
      "position": 43,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DFSEVSNVQ",
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
              "1979": 1,
              "2012": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
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
      "position": 44,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "FSEVSNVQR",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 45,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SEVSNVQRL",
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
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 46,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "EVSNVQRLM",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 47,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VSNVQRLMR",
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
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
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
      "position": 48,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SNVQRLMRK",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 49,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NVQRLMRKE",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 50,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VQRLMRKER",
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
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 51,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QRLMRKERR",
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
      "position": 52,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RLMRKERRD",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 53,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LMRKERRDD",
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
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 54,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "MRKERRDDN",
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
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 55,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RKERRDDND",
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
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
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
      "position": 56,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KERRDDNDL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 57,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ERRDDNDLK",
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
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 58,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RRDDNDLKR",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 59,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RDDNDLKRL",
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
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 60,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DDNDLKRLR",
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
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 61,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DNDLKRLRD",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 62,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NDLKRLRDL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
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
      "position": 63,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DLKRLRDLN",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 64,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LKRLRDLNQ",
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
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 65,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KRLRDLNQA",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 66,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RLRDLNQAV",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
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
      "position": 67,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LRDLNQAVN",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 68,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RDLNQAVNN",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 69,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DLNQAVNNL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
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
      "position": 70,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LNQAVNNLV",
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
      "position": 71,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NQAVNNLVE",
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
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 72,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QAVNNLVEL",
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
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 73,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AVNNLVELK",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 74,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VNNLVELKS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
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
      "position": 75,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NNLVELKST",
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
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 76,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NLVELKSTQ",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 77,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LVELKSTQQ",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 78,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VELKSTQQK",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
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
      "position": 79,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ELKSTQQKS",
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
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 80,
      "low_support": true,
      "entropy": 0.9189692185014229,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "LKSTQQKSI",
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
        },
        {
          "sequence": "LKSTQQKSV",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1979": 1,
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            }
          }
        }
      ]
    },
    {
      "position": 81,
      "low_support": true,
      "entropy": 0.9124400626474368,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "KSTQQKSVL",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "date": {
              "1980": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 2
            }
          }
        },
        {
          "sequence": "KSTQQKSIL",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "date": {
              "2012": 1
            },
            "accession": {
              "QEP52131.1": 1
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
      "position": 82,
      "low_support": true,
      "entropy": 0.9168986948612918,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "STQQKSILR",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "strain": {
              "Sierra Leone": 1
            },
            "date": {
              "2012": 1
            },
            "accession": {
              "QEP52131.1": 1
            },
            "species": {
              "Homo sapiens": 1
            }
          }
        },
        {
          "sequence": "STQQKSVLR",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "date": {
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 83,
      "low_support": true,
      "entropy": 0.9212185391260431,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "TQQKSVLRV",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 2
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1
            }
          }
        },
        {
          "sequence": "TQQKSILRV",
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
            "accession": {
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 84,
      "low_support": true,
      "entropy": 0.9278450546374056,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "QQKSILRVG",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "accession": {
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1
            },
            "strain": {
              "Sierra Leone": 1
            },
            "species": {
              "Homo sapiens": 1
            }
          }
        },
        {
          "sequence": "QQKSVLRVG",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 2
            }
          }
        }
      ]
    },
    {
      "position": 85,
      "low_support": true,
      "entropy": 0.9240224715947949,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "QKSILRVGT",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "species": {
              "Homo sapiens": 1
            },
            "accession": {
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 1
            },
            "date": {
              "2012": 1
            }
          }
        },
        {
          "sequence": "QKSVLRVGT",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1980": 1,
              "1979": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            }
          }
        }
      ]
    },
    {
      "position": 86,
      "low_support": true,
      "entropy": 0.9117274632226768,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "KSVLRVGTL",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 2
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1
            }
          }
        },
        {
          "sequence": "KSILRVGTL",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "species": {
              "Homo sapiens": 1
            },
            "accession": {
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1
            },
            "strain": {
              "Sierra Leone": 1
            }
          }
        }
      ]
    },
    {
      "position": 87,
      "low_support": true,
      "entropy": 0.9197007782130442,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "SILRVGTLT",
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
            "accession": {
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1
            }
          }
        },
        {
          "sequence": "SVLRVGTLT",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 2
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 88,
      "low_support": true,
      "entropy": 0.9226350424143189,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "ILRVGTLTS",
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
        },
        {
          "sequence": "VLRVGTLTS",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "date": {
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 89,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LRVGTLTSD",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 90,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RVGTLTSDD",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 91,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VGTLTSDDL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 92,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GTLTSDDLL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
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
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 93,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TLTSDDLLI",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
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
      "position": 94,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LTSDDLLIL",
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
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 95,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TSDDLLILA",
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
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 96,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SDDLLILAA",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 97,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DDLLILAAD",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
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
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 98,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DLLILAADL",
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
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 99,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LLILAADLE",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
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
      "position": 100,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LILAADLEK",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
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
      "position": 101,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ILAADLEKL",
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
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
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
      "position": 102,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LAADLEKLK",
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
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 103,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AADLEKLKS",
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
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 104,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ADLEKLKSK",
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
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 105,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DLEKLKSKV",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
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
      "position": 106,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LEKLKSKVT",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 107,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "EKLKSKVTR",
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
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
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
      "position": 108,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KLKSKVTRT",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 109,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LKSKVTRTE",
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
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 110,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KSKVTRTER",
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
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 111,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SKVTRTERP",
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
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 112,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KVTRTERPL",
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
            }
          }
        }
      ]
    },
    {
      "position": 113,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VTRTERPLS",
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
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 114,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TRTERPLSA",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 115,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RTERPLSAG",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 116,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TERPLSAGV",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 117,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ERPLSAGVY",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
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
      "position": 118,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RPLSAGVYM",
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
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
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
      "position": 119,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "PLSAGVYMG",
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
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
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
      "position": 120,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LSAGVYMGN",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 121,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SAGVYMGNL",
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
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 122,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AGVYMGNLS",
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
      "position": 123,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GVYMGNLSS",
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
              "1979": 1,
              "2012": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 124,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VYMGNLSSQ",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
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
      "position": 125,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "YMGNLSSQQ",
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
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 126,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "MGNLSSQQL",
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
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
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
      "position": 127,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GNLSSQQLD",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 128,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NLSSQQLDQ",
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
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
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
      "position": 129,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LSSQQLDQR",
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
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 130,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SSQQLDQRR",
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
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
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
      "position": 131,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SQQLDQRRA",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
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
      "position": 132,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QQLDQRRAL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 133,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QLDQRRALL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 134,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LDQRRALLS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
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
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 135,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DQRRALLSM",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 136,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QRRALLSMI",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 137,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RRALLSMIG",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
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
      "position": 138,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RALLSMIGM",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
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
      "position": 139,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ALLSMIGMS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 140,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LLSMIGMSG",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 141,
      "low_support": true,
      "entropy": 0.9136019432743042,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "LSMIGMSGS",
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
            "species": {
              "Homo sapiens": 1
            },
            "accession": {
              "QEP52131.1": 1
            }
          }
        },
        {
          "sequence": "LSMIGMSGG",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "date": {
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 142,
      "low_support": true,
      "entropy": 0.9188804991662839,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "SMIGMSGGN",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "date": {
              "1980": 1,
              "1979": 1
            }
          }
        },
        {
          "sequence": "SMIGMSGSN",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "date": {
              "2012": 1
            },
            "species": {
              "Homo sapiens": 1
            },
            "accession": {
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 1
            }
          }
        }
      ]
    },
    {
      "position": 143,
      "low_support": true,
      "entropy": 0.9171458552063146,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "MIGMSGSNQ",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "strain": {
              "Sierra Leone": 1
            },
            "date": {
              "2012": 1
            },
            "species": {
              "Homo sapiens": 1
            },
            "accession": {
              "QEP52131.1": 1
            }
          }
        },
        {
          "sequence": "MIGMSGGNQ",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 2
            },
            "date": {
              "1979": 1,
              "1980": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            }
          }
        }
      ]
    },
    {
      "position": 144,
      "low_support": true,
      "entropy": 0.9137561057710887,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "IGMSGGNQG",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "date": {
              "1980": 1,
              "1979": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 2
            }
          }
        },
        {
          "sequence": "IGMSGSNQG",
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
            "accession": {
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 145,
      "low_support": true,
      "entropy": 0.9189600964150592,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "GMSGGNQGA",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "1980": 1,
              "1979": 1
            }
          }
        },
        {
          "sequence": "GMSGSNQGA",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "species": {
              "Homo sapiens": 1
            },
            "accession": {
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 1
            },
            "date": {
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 146,
      "low_support": true,
      "entropy": 0.9216262444809887,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "MSGGNQGAQ",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1979": 1,
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            }
          }
        },
        {
          "sequence": "MSGSNQGAR",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "accession": {
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1
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
      "position": 147,
      "low_support": true,
      "entropy": 0.9178209468465276,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "SGGNQGAQA",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "date": {
              "1979": 1,
              "1980": 1
            }
          }
        },
        {
          "sequence": "SGSNQGARA",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "date": {
              "2012": 1
            },
            "accession": {
              "QEP52131.1": 1
            },
            "species": {
              "Homo sapiens": 1
            },
            "strain": {
              "Sierra Leone": 1
            }
          }
        }
      ]
    },
    {
      "position": 148,
      "low_support": true,
      "entropy": 0.9120486513538161,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "GSNQGARAG",
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
        },
        {
          "sequence": "GGNQGAQAG",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 2
            }
          }
        }
      ]
    },
    {
      "position": 149,
      "low_support": true,
      "entropy": 0.9159518635117221,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "SNQGARAGR",
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
            "accession": {
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1
            }
          }
        },
        {
          "sequence": "GNQGAQAGR",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "date": {
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 150,
      "low_support": true,
      "entropy": 0.9132197364073764,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "NQGAQAGRD",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 2
            }
          }
        },
        {
          "sequence": "NQGARAGRD",
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
            "accession": {
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 151,
      "low_support": true,
      "entropy": 0.9197756501956436,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "QGAQAGRDG",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 2
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "date": {
              "1979": 1,
              "1980": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            }
          }
        },
        {
          "sequence": "QGARAGRDG",
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
    },
    {
      "position": 152,
      "low_support": true,
      "entropy": 0.9191799419574659,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "GAQAGRDGV",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "date": {
              "1980": 1,
              "1979": 1
            }
          }
        },
        {
          "sequence": "GARAGRDGV",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "strain": {
              "Sierra Leone": 1
            },
            "date": {
              "2012": 1
            },
            "species": {
              "Homo sapiens": 1
            },
            "accession": {
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 153,
      "low_support": true,
      "entropy": 0.9195896210573261,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "AQAGRDGVV",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "date": {
              "1980": 1,
              "1979": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            }
          }
        },
        {
          "sequence": "ARAGRDGVV",
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
            "strain": {
              "Sierra Leone": 1
            },
            "accession": {
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 154,
      "low_support": true,
      "entropy": 0.9169666682872607,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "RAGRDGVVR",
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
            "accession": {
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1
            }
          }
        },
        {
          "sequence": "QAGRDGVVR",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "date": {
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 155,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AGRDGVVRV",
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
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 156,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GRDGVVRVW",
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
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 157,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RDGVVRVWD",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 158,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DGVVRVWDV",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
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
      "position": 159,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GVVRVWDVK",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 160,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VVRVWDVKN",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 161,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VRVWDVKNA",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
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
      "position": 162,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RVWDVKNAE",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 163,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VWDVKNAEL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 164,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "WDVKNAELL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 165,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DVKNAELLN",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
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
      "position": 166,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VKNAELLNN",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 167,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KNAELLNNQ",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
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
      "position": 168,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NAELLNNQF",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
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
      "position": 169,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AELLNNQFG",
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
      "position": 170,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ELLNNQFGT",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 171,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LLNNQFGTM",
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
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 172,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LNNQFGTMP",
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
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 173,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NNQFGTMPS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 174,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NQFGTMPSL",
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
              "QEP52131.1": 1,
              "AYD75325.1": 1,
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
      "position": 175,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QFGTMPSLT",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 176,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "FGTMPSLTL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
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
      "position": 177,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GTMPSLTLA",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
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
      "position": 178,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TMPSLTLAC",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 179,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "MPSLTLACL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
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
      "position": 180,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "PSLTLACLT",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 181,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SLTLACLTK",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
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
      "position": 182,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LTLACLTKQ",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 183,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TLACLTKQG",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 184,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LACLTKQGQ",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
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
      "position": 185,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ACLTKQGQV",
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
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
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
      "position": 186,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "CLTKQGQVD",
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
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
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
      "position": 187,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LTKQGQVDL",
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
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1980": 1,
              "1979": 1,
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
      "position": 188,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TKQGQVDLN",
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
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 189,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KQGQVDLND",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 190,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QGQVDLNDA",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 191,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GQVDLNDAV",
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
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 192,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QVDLNDAVQ",
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
            }
          }
        }
      ]
    },
    {
      "position": 193,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VDLNDAVQA",
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
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 194,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DLNDAVQAL",
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
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
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
      "position": 195,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LNDAVQALT",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 196,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NDAVQALTD",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 197,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DAVQALTDL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 198,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AVQALTDLG",
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
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 199,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VQALTDLGL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
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
      "position": 200,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QALTDLGLI",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 201,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ALTDLGLIY",
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
              "1979": 1,
              "2012": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 202,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LTDLGLIYT",
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
      "position": 203,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TDLGLIYTA",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
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
      "position": 204,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DLGLIYTAK",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
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
      "position": 205,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LGLIYTAKY",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 206,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GLIYTAKYP",
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
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 207,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LIYTAKYPN",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
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
      "position": 208,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "IYTAKYPNT",
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
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 209,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "YTAKYPNTS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 210,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TAKYPNTSD",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 211,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AKYPNTSDL",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 212,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KYPNTSDLD",
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
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 213,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "YPNTSDLDR",
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
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 214,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "PNTSDLDRL",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 215,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NTSDLDRLT",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 216,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TSDLDRLTQ",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 217,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SDLDRLTQS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
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
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 218,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DLDRLTQSH",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
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
            }
          }
        }
      ]
    },
    {
      "position": 219,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LDRLTQSHP",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 220,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DRLTQSHPI",
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
              "1980": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 221,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RLTQSHPIL",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 222,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LTQSHPILN",
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
              "1980": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 223,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TQSHPILNM",
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
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 224,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QSHPILNMI",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
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
      "position": 225,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SHPILNMID",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 226,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "HPILNMIDT",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
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
      "position": 227,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "PILNMIDTK",
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
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 228,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ILNMIDTKK",
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
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
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
      "position": 229,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LNMIDTKKS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 230,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NMIDTKKSS",
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
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 231,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "MIDTKKSSL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 232,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "IDTKKSSLN",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 233,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DTKKSSLNI",
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
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 234,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TKKSSLNIS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
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
      "position": 235,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KKSSLNISG",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 236,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KSSLNISGY",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
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
            }
          }
        }
      ]
    },
    {
      "position": 237,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SSLNISGYN",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 238,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SLNISGYNF",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 239,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LNISGYNFS",
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
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 240,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NISGYNFSL",
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
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 241,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ISGYNFSLG",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 242,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SGYNFSLGA",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 243,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GYNFSLGAA",
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
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
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
      "position": 244,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "YNFSLGAAV",
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
      "position": 245,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NFSLGAAVK",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 246,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "FSLGAAVKA",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
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
      "position": 247,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SLGAAVKAG",
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
            }
          }
        }
      ]
    },
    {
      "position": 248,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LGAAVKAGA",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 249,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GAAVKAGAC",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 250,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AAVKAGACM",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 251,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AVKAGACML",
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
            }
          }
        }
      ]
    },
    {
      "position": 252,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VKAGACMLD",
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
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 253,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KAGACMLDG",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
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
      "position": 254,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AGACMLDGG",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 255,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GACMLDGGN",
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
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
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
      "position": 256,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ACMLDGGNM",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
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
      "position": 257,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "CMLDGGNML",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 258,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "MLDGGNMLE",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 259,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LDGGNMLET",
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
      "position": 260,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DGGNMLETI",
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
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 261,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GGNMLETIK",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 262,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GNMLETIKV",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 263,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NMLETIKVS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
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
      "position": 264,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "MLETIKVSP",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 265,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LETIKVSPQ",
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
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
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
      "position": 266,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ETIKVSPQT",
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
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 267,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TIKVSPQTM",
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
      "position": 268,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "IKVSPQTMD",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
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
      "position": 269,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KVSPQTMDG",
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
      "position": 270,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VSPQTMDGI",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 271,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SPQTMDGIL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 272,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "PQTMDGILK",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
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
      "position": 273,
      "low_support": true,
      "entropy": 0.0,
      "support": 0,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": null
    },
    {
      "position": 274,
      "low_support": true,
      "entropy": 0.0,
      "support": 0,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": null
    },
    {
      "position": 275,
      "low_support": true,
      "entropy": 0.0,
      "support": 0,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": null
    },
    {
      "position": 276,
      "low_support": true,
      "entropy": 0.0,
      "support": 0,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": null
    },
    {
      "position": 277,
      "low_support": true,
      "entropy": 0.0,
      "support": 0,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": null
    },
    {
      "position": 278,
      "low_support": true,
      "entropy": 0.0,
      "support": 0,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": null
    },
    {
      "position": 279,
      "low_support": true,
      "entropy": 0.0,
      "support": 0,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": null
    },
    {
      "position": 280,
      "low_support": true,
      "entropy": 0.0,
      "support": 0,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": null
    },
    {
      "position": 281,
      "low_support": true,
      "entropy": 0.0,
      "support": 0,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": null
    },
    {
      "position": 282,
      "low_support": true,
      "entropy": 0.0,
      "support": 0,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": null
    },
    {
      "position": 283,
      "low_support": true,
      "entropy": 0.0,
      "support": 0,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": null
    },
    {
      "position": 284,
      "low_support": true,
      "entropy": 0.0,
      "support": 0,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": null
    },
    {
      "position": 285,
      "low_support": true,
      "entropy": 0.0,
      "support": 0,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": null
    },
    {
      "position": 286,
      "low_support": true,
      "entropy": 0.0,
      "support": 0,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": null
    },
    {
      "position": 287,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SILKVKKAL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
              "1980": 1,
              "1979": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 288,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ILKVKKALG",
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
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
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
      "position": 289,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LKVKKALGM",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 290,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KVKKALGMF",
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
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
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
      "position": 291,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VKKALGMFI",
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
      "position": 292,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KKALGMFIS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 293,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KALGMFISD",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
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
      "position": 294,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ALGMFISDT",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
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
      "position": 295,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LGMFISDTP",
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
      "position": 296,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GMFISDTPG",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
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
      "position": 297,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "MFISDTPGE",
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
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 298,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "FISDTPGER",
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
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 299,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ISDTPGERN",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 300,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SDTPGERNP",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 301,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DTPGERNPY",
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
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
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
      "position": 302,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TPGERNPYE",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 303,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "PGERNPYEN",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
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
      "position": 304,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GERNPYENI",
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
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 305,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ERNPYENIL",
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
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 306,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RNPYENILY",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
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
      "position": 307,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NPYENILYK",
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
              "AYD75365.1": 1,
              "QEP52131.1": 1
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
      "position": 308,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "PYENILYKI",
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
              "AYD75365.1": 1,
              "QEP52131.1": 1
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
      "position": 309,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "YENILYKIC",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 310,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ENILYKICL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
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
      "position": 311,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NILYKICLS",
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
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 312,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ILYKICLSG",
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
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 313,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LYKICLSGD",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
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
      "position": 314,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "YKICLSGDG",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
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
      "position": 315,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KICLSGDGW",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 316,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ICLSGDGWP",
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
            }
          }
        }
      ]
    },
    {
      "position": 317,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "CLSGDGWPY",
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
              "AYD75365.1": 1,
              "QEP52131.1": 1
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
      "position": 318,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LSGDGWPYI",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
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
      "position": 319,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SGDGWPYIA",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 320,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GDGWPYIAS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
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
      "position": 321,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DGWPYIASR",
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
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 322,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GWPYIASRT",
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
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
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
      "position": 323,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "WPYIASRTS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
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
      "position": 324,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "PYIASRTSI",
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
      "position": 325,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "YIASRTSIT",
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
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 326,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "IASRTSITG",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
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
      "position": 327,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ASRTSITGR",
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
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 328,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SRTSITGRA",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
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
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 329,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RTSITGRAW",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 330,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TSITGRAWE",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 331,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SITGRAWEN",
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
              "1979": 1,
              "1980": 1
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
      "position": 332,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ITGRAWENT",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 333,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TGRAWENTV",
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
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
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
      "position": 334,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GRAWENTVV",
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
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 335,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RAWENTVVD",
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
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 336,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AWENTVVDL",
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
      "position": 337,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "WENTVVDLE",
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
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 338,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ENTVVDLES",
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
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
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
      "position": 339,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NTVVDLESD",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 340,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TVVDLESDG",
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
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 341,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VVDLESDGK",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 342,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VDLESDGKP",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 343,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DLESDGKPQ",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1979": 1,
              "2012": 1,
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
      "position": 344,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LESDGKPQK",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
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
      "position": 345,
      "low_support": true,
      "entropy": 0.9195049377162688,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "ESDGKPQKT",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "date": {
              "1979": 1,
              "1980": 1
            }
          }
        },
        {
          "sequence": "ESDGKPQKA",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "accession": {
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1
            },
            "species": {
              "Homo sapiens": 1
            },
            "strain": {
              "Sierra Leone": 1
            }
          }
        }
      ]
    },
    {
      "position": 346,
      "low_support": true,
      "entropy": 0.9167614632613577,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "SDGKPQKAG",
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
            "species": {
              "Homo sapiens": 1
            },
            "accession": {
              "QEP52131.1": 1
            }
          }
        },
        {
          "sequence": "SDGKPQKTG",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 2
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "date": {
              "1979": 1,
              "1980": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 347,
      "low_support": true,
      "entropy": 0.9188248416228881,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "DGKPQKAGS",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "strain": {
              "Sierra Leone": 1
            },
            "date": {
              "2012": 1
            },
            "accession": {
              "QEP52131.1": 1
            },
            "species": {
              "Homo sapiens": 1
            }
          }
        },
        {
          "sequence": "DGKPQKTGN",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "date": {
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 348,
      "low_support": true,
      "entropy": 0.9194722857877541,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "GKPQKAGSN",
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
              "2012": 1
            },
            "accession": {
              "QEP52131.1": 1
            }
          }
        },
        {
          "sequence": "GKPQKTGNN",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "date": {
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 349,
      "low_support": true,
      "entropy": 1.5899608494368642,
      "support": 3,
      "distinct_variants_count": 3,
      "distinct_variants_incidence": 100.0,
      "variants": [
        {
          "sequence": "KPQKAGSNN",
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
            "date": {
              "2012": 1
            },
            "species": {
              "Homo sapiens": 1
            }
          }
        },
        {
          "sequence": "KPQKTGNNN",
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
            "date": {
              "1979": 1
            },
            "accession": {
              "AYD75325.1": 1
            }
          }
        },
        {
          "sequence": "KPQKTGNNS",
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
            "date": {
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 1
            }
          }
        }
      ]
    },
    {
      "position": 350,
      "low_support": true,
      "entropy": 1.5879960866176654,
      "support": 3,
      "distinct_variants_count": 3,
      "distinct_variants_incidence": 100.0,
      "variants": [
        {
          "sequence": "PQKAGSNNS",
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
        },
        {
          "sequence": "PQKTGNNNS",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "strain": {
              "Sierra Leone": 1
            },
            "accession": {
              "AYD75325.1": 1
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
          "sequence": "PQKTGNNSS",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "date": {
              "1980": 1
            },
            "accession": {
              "AYD75365.1": 1
            },
            "species": {
              "Homo sapiens": 1
            },
            "strain": {
              "Sierra Leone": 1
            }
          }
        }
      ]
    },
    {
      "position": 351,
      "low_support": true,
      "entropy": 1.5873026857324077,
      "support": 3,
      "distinct_variants_count": 3,
      "distinct_variants_incidence": 100.0,
      "variants": [
        {
          "sequence": "QKAGSNNSN",
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
            "date": {
              "2012": 1
            },
            "species": {
              "Homo sapiens": 1
            }
          }
        },
        {
          "sequence": "QKTGNNNSN",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "species": {
              "Unknown": 1
            },
            "accession": {
              "AYD75325.1": 1
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
          "sequence": "QKTGNNSSN",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "date": {
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 1
            },
            "species": {
              "Homo sapiens": 1
            },
            "accession": {
              "AYD75365.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 352,
      "low_support": true,
      "entropy": 1.5901618841263412,
      "support": 3,
      "distinct_variants_count": 3,
      "distinct_variants_incidence": 100.0,
      "variants": [
        {
          "sequence": "KTGNNNSNK",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "date": {
              "1979": 1
            },
            "accession": {
              "AYD75325.1": 1
            },
            "species": {
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 1
            }
          }
        },
        {
          "sequence": "KTGNNSSNK",
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
        },
        {
          "sequence": "KAGSNNSNK",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "date": {
              "2012": 1
            },
            "species": {
              "Homo sapiens": 1
            },
            "strain": {
              "Sierra Leone": 1
            },
            "accession": {
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 353,
      "low_support": true,
      "entropy": 1.583875440071502,
      "support": 3,
      "distinct_variants_count": 3,
      "distinct_variants_incidence": 100.0,
      "variants": [
        {
          "sequence": "TGNNSSNKS",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "species": {
              "Homo sapiens": 1
            },
            "accession": {
              "AYD75365.1": 1
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
          "sequence": "TGNNNSNKS",
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
          "sequence": "AGSNNSNKS",
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
              "2012": 1
            },
            "accession": {
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 354,
      "low_support": true,
      "entropy": 1.5867987066390608,
      "support": 3,
      "distinct_variants_count": 3,
      "distinct_variants_incidence": 100.0,
      "variants": [
        {
          "sequence": "GNNSSNKSL",
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
        },
        {
          "sequence": "GSNNSNKSL",
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
            "date": {
              "2012": 1
            },
            "species": {
              "Homo sapiens": 1
            }
          }
        },
        {
          "sequence": "GNNNSNKSL",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "date": {
              "1979": 1
            },
            "species": {
              "Unknown": 1
            },
            "accession": {
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 1
            }
          }
        }
      ]
    },
    {
      "position": 355,
      "low_support": true,
      "entropy": 1.5848467659058636,
      "support": 3,
      "distinct_variants_count": 3,
      "distinct_variants_incidence": 100.0,
      "variants": [
        {
          "sequence": "SNNSNKSLQ",
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
            "species": {
              "Homo sapiens": 1
            },
            "accession": {
              "QEP52131.1": 1
            }
          }
        },
        {
          "sequence": "NNNSNKSLQ",
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
            "date": {
              "1979": 1
            },
            "accession": {
              "AYD75325.1": 1
            }
          }
        },
        {
          "sequence": "NNSSNKSLQ",
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
      "position": 356,
      "low_support": true,
      "entropy": 0.9157935310495522,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "NNSNKSLQS",
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
              "2012": 1,
              "1979": 1
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 2
            }
          }
        },
        {
          "sequence": "NSSNKSLQS",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "strain": {
              "Sierra Leone": 1
            },
            "accession": {
              "AYD75365.1": 1
            },
            "date": {
              "1980": 1
            },
            "species": {
              "Homo sapiens": 1
            }
          }
        }
      ]
    },
    {
      "position": 357,
      "low_support": true,
      "entropy": 0.9193526617346596,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "SSNKSLQSA",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "species": {
              "Homo sapiens": 1
            },
            "date": {
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 1
            },
            "accession": {
              "AYD75365.1": 1
            }
          }
        },
        {
          "sequence": "NSNKSLQSA",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "date": {
              "1979": 1,
              "2012": 1
            },
            "strain": {
              "Sierra Leone": 2
            }
          }
        }
      ]
    },
    {
      "position": 358,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SNKSLQSAG",
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
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
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
      "position": 359,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NKSLQSAGF",
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
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
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
      "position": 360,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KSLQSAGFT",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 361,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SLQSAGFTA",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 362,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LQSAGFTAG",
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
              "1979": 1,
              "1980": 1
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
      "position": 363,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QSAGFTAGL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 364,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SAGFTAGLT",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 365,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AGFTAGLTY",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 366,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GFTAGLTYS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 367,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "FTAGLTYSQ",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 368,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TAGLTYSQL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
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
      "position": 369,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AGLTYSQLM",
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
      "position": 370,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GLTYSQLMT",
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
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
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
      "position": 371,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LTYSQLMTL",
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
      "position": 372,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TYSQLMTLK",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 373,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "YSQLMTLKD",
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
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 374,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SQLMTLKDA",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
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
      "position": 375,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QLMTLKDAM",
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
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 376,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LMTLKDAML",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 377,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "MTLKDAMLQ",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 378,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TLKDAMLQL",
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
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 379,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LKDAMLQLD",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 380,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KDAMLQLDP",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
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
      "position": 381,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DAMLQLDPN",
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
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 382,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AMLQLDPNA",
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
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
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
      "position": 383,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "MLQLDPNAK",
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
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 384,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LQLDPNAKT",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
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
      "position": 385,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QLDPNAKTW",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 386,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LDPNAKTWM",
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
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 387,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DPNAKTWMD",
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
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
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
      "position": 388,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "PNAKTWMDI",
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
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 389,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NAKTWMDIE",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 390,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AKTWMDIEG",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 391,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KTWMDIEGR",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 392,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TWMDIEGRP",
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
              "1980": 1,
              "2012": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 393,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "WMDIEGRPE",
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
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 394,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "MDIEGRPED",
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
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 395,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DIEGRPEDP",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
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
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 396,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "IEGRPEDPV",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
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
      "position": 397,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "EGRPEDPVE",
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
              "AYD75365.1": 1,
              "QEP52131.1": 1
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
      "position": 398,
      "low_support": true,
      "entropy": 0.9238669278249693,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "GRPEDPVEV",
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
            "accession": {
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1
            }
          }
        },
        {
          "sequence": "GRPEDPVEI",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "date": {
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 399,
      "low_support": true,
      "entropy": 0.9234775412081652,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "RPEDPVEIA",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1979": 1,
              "1980": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            }
          }
        },
        {
          "sequence": "RPEDPVEVA",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "accession": {
              "QEP52131.1": 1
            },
            "species": {
              "Homo sapiens": 1
            },
            "strain": {
              "Sierra Leone": 1
            },
            "date": {
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 400,
      "low_support": true,
      "entropy": 0.9188941006591103,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "PEDPVEVAL",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "strain": {
              "Sierra Leone": 1
            },
            "date": {
              "2012": 1
            },
            "accession": {
              "QEP52131.1": 1
            },
            "species": {
              "Homo sapiens": 1
            }
          }
        },
        {
          "sequence": "PEDPVEIAL",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 2
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 401,
      "low_support": true,
      "entropy": 0.912167336357988,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "EDPVEVALY",
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
          "sequence": "EDPVEIALY",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "date": {
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 402,
      "low_support": true,
      "entropy": 0.918270029981237,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "DPVEIALYQ",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            }
          }
        },
        {
          "sequence": "DPVEVALYQ",
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
            "strain": {
              "Sierra Leone": 1
            },
            "accession": {
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 403,
      "low_support": true,
      "entropy": 0.9115167181005103,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "PVEIALYQP",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1980": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            }
          }
        },
        {
          "sequence": "PVEVALYQP",
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
      "position": 404,
      "low_support": true,
      "entropy": 0.9317138694332231,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "VEIALYQPS",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "date": {
              "1980": 1,
              "1979": 1
            }
          }
        },
        {
          "sequence": "VEVALYQPS",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "strain": {
              "Sierra Leone": 1
            },
            "date": {
              "2012": 1
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
    },
    {
      "position": 405,
      "low_support": true,
      "entropy": 0.9272504344197905,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "EIALYQPSS",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "date": {
              "1980": 1,
              "1979": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            }
          }
        },
        {
          "sequence": "EVALYQPSS",
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
    },
    {
      "position": 406,
      "low_support": true,
      "entropy": 0.9163687813672482,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "VALYQPSSG",
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
        },
        {
          "sequence": "IALYQPSSG",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "date": {
              "1979": 1,
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 2
            }
          }
        }
      ]
    },
    {
      "position": 407,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ALYQPSSGC",
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
      "position": 408,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LYQPSSGCY",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
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
      "position": 409,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "YQPSSGCYI",
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
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
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
      "position": 410,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QPSSGCYIH",
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
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 411,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "PSSGCYIHF",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
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
      "position": 412,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SSGCYIHFF",
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
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
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
      "position": 413,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SGCYIHFFR",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 414,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GCYIHFFRE",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 415,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "CYIHFFREP",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 416,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "YIHFFREPT",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 417,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "IHFFREPTD",
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
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 418,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "HFFREPTDL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 419,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "FFREPTDLK",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
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
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            }
          }
        }
      ]
    },
    {
      "position": 420,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "FREPTDLKQ",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 421,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "REPTDLKQF",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 422,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "EPTDLKQFK",
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
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 423,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "PTDLKQFKQ",
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
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
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
      "position": 424,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TDLKQFKQD",
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
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 425,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DLKQFKQDA",
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
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
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
      "position": 426,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LKQFKQDAK",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
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
      "position": 427,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KQFKQDAKY",
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
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 428,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QFKQDAKYS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
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
            }
          }
        }
      ]
    },
    {
      "position": 429,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "FKQDAKYSH",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 430,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KQDAKYSHG",
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
              "1980": 1,
              "1979": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 431,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QDAKYSHGI",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 432,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DAKYSHGID",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 433,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AKYSHGIDV",
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
            "strain": {
              "Sierra Leone": 3
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
      "position": 434,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KYSHGIDVT",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 435,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "YSHGIDVTD",
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
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 436,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SHGIDVTDL",
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
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 437,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "HGIDVTDLF",
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
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
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
      "position": 438,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GIDVTDLFA",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 439,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "IDVTDLFAA",
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
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
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
      "position": 440,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DVTDLFAAQ",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 441,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VTDLFAAQP",
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
              "1979": 1,
              "2012": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
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
      "position": 442,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TDLFAAQPG",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
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
      "position": 443,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DLFAAQPGL",
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
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 444,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LFAAQPGLT",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 445,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "FAAQPGLTS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 446,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AAQPGLTSA",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 447,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AQPGLTSAV",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 448,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QPGLTSAVI",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
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
      "position": 449,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "PGLTSAVID",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
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
      "position": 450,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GLTSAVIDA",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 451,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LTSAVIDAL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
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
      "position": 452,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TSAVIDALP",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
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
      "position": 453,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SAVIDALPR",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 454,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AVIDALPRN",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 455,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VIDALPRNM",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 456,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "IDALPRNMV",
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
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 457,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DALPRNMVI",
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
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 458,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ALPRNMVIT",
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
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 459,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LPRNMVITC",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 460,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "PRNMVITCQ",
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
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 461,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RNMVITCQG",
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
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 462,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NMVITCQGS",
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
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 463,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "MVITCQGSD",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
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
      "position": 464,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VITCQGSDD",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 465,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ITCQGSDDI",
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
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 466,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TCQGSDDIR",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 467,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "CQGSDDIRK",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
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
      "position": 468,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QGSDDIRKL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 469,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GSDDIRKLL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 470,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SDDIRKLLE",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 471,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DDIRKLLES",
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
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 472,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DIRKLLESQ",
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
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
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
      "position": 473,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "IRKLLESQG",
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
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
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
      "position": 474,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RKLLESQGR",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 475,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KLLESQGRK",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 476,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LLESQGRKD",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
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
      "position": 477,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LESQGRKDI",
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
              "1979": 1,
              "2012": 1
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
      "position": 478,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ESQGRKDIK",
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
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 479,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SQGRKDIKL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
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
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 480,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QGRKDIKLI",
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
      "position": 481,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GRKDIKLID",
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
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
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
      "position": 482,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RKDIKLIDI",
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
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 483,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KDIKLIDIA",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 484,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DIKLIDIAL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 485,
      "low_support": true,
      "entropy": 0.9123479788731494,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "IKLIDIALN",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "1980": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 2
            }
          }
        },
        {
          "sequence": "IKLIDIALS",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "accession": {
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1
            },
            "species": {
              "Homo sapiens": 1
            },
            "strain": {
              "Sierra Leone": 1
            }
          }
        }
      ]
    },
    {
      "position": 486,
      "low_support": true,
      "entropy": 0.9209516351432795,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "KLIDIALSK",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "accession": {
              "QEP52131.1": 1
            },
            "species": {
              "Homo sapiens": 1
            },
            "date": {
              "2012": 1
            },
            "strain": {
              "Sierra Leone": 1
            }
          }
        },
        {
          "sequence": "KLIDIALNK",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            }
          }
        }
      ]
    },
    {
      "position": 487,
      "low_support": true,
      "entropy": 0.9140099431105404,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "LIDIALSKT",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "accession": {
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1
            },
            "strain": {
              "Sierra Leone": 1
            },
            "species": {
              "Homo sapiens": 1
            }
          }
        },
        {
          "sequence": "LIDIALNKT",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 488,
      "low_support": true,
      "entropy": 0.9091417508619442,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "IDIALSKTD",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "strain": {
              "Sierra Leone": 1
            },
            "date": {
              "2012": 1
            },
            "species": {
              "Homo sapiens": 1
            },
            "accession": {
              "QEP52131.1": 1
            }
          }
        },
        {
          "sequence": "IDIALNKTD",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1979": 1,
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            }
          }
        }
      ]
    },
    {
      "position": 489,
      "low_support": true,
      "entropy": 0.9186340100055176,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "DIALSKTDS",
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
          "sequence": "DIALNKTDS",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "date": {
              "1980": 1,
              "1979": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 2
            }
          }
        }
      ]
    },
    {
      "position": 490,
      "low_support": true,
      "entropy": 0.9099329837308432,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "IALNKTDSR",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "date": {
              "1979": 1,
              "1980": 1
            }
          }
        },
        {
          "sequence": "IALSKTDSR",
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
            "accession": {
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 491,
      "low_support": true,
      "entropy": 0.91829887478341,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "ALSKTDSRK",
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
          "sequence": "ALNKTDSRK",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            },
            "date": {
              "1980": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 2
            }
          }
        }
      ]
    },
    {
      "position": 492,
      "low_support": true,
      "entropy": 0.9155483689478582,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "LNKTDSRKY",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 2
            },
            "date": {
              "1979": 1,
              "1980": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 1
            }
          }
        },
        {
          "sequence": "LSKTDSRKY",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "date": {
              "2012": 1
            },
            "accession": {
              "QEP52131.1": 1
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
      "position": 493,
      "low_support": true,
      "entropy": 0.9235844772997628,
      "support": 3,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 33.333336,
      "variants": [
        {
          "sequence": "SKTDSRKYE",
          "count": 1,
          "incidence": 33.333336,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "species": {
              "Homo sapiens": 1
            },
            "accession": {
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 1
            },
            "date": {
              "2012": 1
            }
          }
        },
        {
          "sequence": "NKTDSRKYE",
          "count": 2,
          "incidence": 66.66667,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 2
            },
            "species": {
              "Homo sapiens": 1,
              "Unknown": 1
            },
            "date": {
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 494,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KTDSRKYEN",
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
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 495,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TDSRKYENA",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 496,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DSRKYENAV",
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
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 497,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SRKYENAVW",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
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
      "position": 498,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RKYENAVWD",
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
              "2012": 1,
              "1979": 1,
              "1980": 1
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
      "position": 499,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KYENAVWDQ",
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
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
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
      "position": 500,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "YENAVWDQY",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
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
      "position": 501,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ENAVWDQYK",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 502,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NAVWDQYKD",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 503,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AVWDQYKDL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 504,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VWDQYKDLC",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 505,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "WDQYKDLCH",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 506,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DQYKDLCHM",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1979": 1,
              "2012": 1,
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
      "position": 507,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "QYKDLCHMH",
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
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 508,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "YKDLCHMHT",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
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
      "position": 509,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KDLCHMHTG",
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
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
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
      "position": 510,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DLCHMHTGV",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
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
      "position": 511,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LCHMHTGVV",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 512,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "CHMHTGVVV",
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
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 513,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "HMHTGVVVE",
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
            }
          }
        }
      ]
    },
    {
      "position": 514,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "MHTGVVVEK",
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
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
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
      "position": 515,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "HTGVVVEKK",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 516,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TGVVVEKKK",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
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
      "position": 517,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GVVVEKKKR",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
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
      "position": 518,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VVVEKKKRG",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
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
      "position": 519,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VVEKKKRGG",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 520,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VEKKKRGGK",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 521,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "EKKKRGGKE",
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
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 522,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KKKRGGKEE",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
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
      "position": 523,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KKRGGKEEI",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
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
      "position": 524,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KRGGKEEIT",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 525,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RGGKEEITP",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
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
      "position": 526,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GGKEEITPH",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 527,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GKEEITPHC",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 528,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "KEEITPHCA",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 529,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "EEITPHCAL",
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
      "position": 530,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "EITPHCALM",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
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
      "position": 531,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ITPHCALMD",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
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
      "position": 532,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TPHCALMDC",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 533,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "PHCALMDCI",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
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
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 534,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "HCALMDCIM",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
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
      "position": 535,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "CALMDCIMF",
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
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 536,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "ALMDCIMFD",
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
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
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
      "position": 537,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LMDCIMFDA",
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
              "QEP52131.1": 1,
              "AYD75365.1": 1,
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
      "position": 538,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "MDCIMFDAA",
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
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 539,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DCIMFDAAV",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
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
      "position": 540,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "CIMFDAAVS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
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
      "position": 541,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "IMFDAAVSG",
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
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
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
      "position": 542,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "MFDAAVSGG",
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
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
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
      "position": 543,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "FDAAVSGGL",
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
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 544,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DAAVSGGLN",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
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
      "position": 545,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AAVSGGLNT",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
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
            }
          }
        }
      ]
    },
    {
      "position": 546,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AVSGGLNTS",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 547,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VSGGLNTSV",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 548,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SGGLNTSVL",
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
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 549,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GGLNTSVLR",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
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
      "position": 550,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "GLNTSVLRA",
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
              "2012": 1,
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
      "position": 551,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LNTSVLRAV",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "2012": 1,
              "1980": 1,
              "1979": 1
            }
          }
        }
      ]
    },
    {
      "position": 552,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "NTSVLRAVL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "1980": 1,
              "2012": 1,
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
      "position": 553,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "TSVLRAVLP",
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
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            }
          }
        }
      ]
    },
    {
      "position": 554,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "SVLRAVLPR",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
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
      "position": 555,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VLRAVLPRD",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "date": {
              "1980": 1,
              "2012": 1,
              "1979": 1
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 556,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LRAVLPRDM",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
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
      "position": 557,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RAVLPRDMV",
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
            "accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 558,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "AVLPRDMVF",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "date": {
              "2012": 1,
              "1979": 1,
              "1980": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 559,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VLPRDMVFR",
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
              "2012": 1,
              "1980": 1,
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
      "position": 560,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "LPRDMVFRT",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
            }
          }
        }
      ]
    },
    {
      "position": 561,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "PRDMVFRTS",
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
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "date": {
              "1980": 1,
              "1979": 1,
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
      "position": 562,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RDMVFRTST",
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
            "date": {
              "1979": 1,
              "1980": 1,
              "2012": 1
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
      "position": 563,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "DMVFRTSTP",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 564,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "MVFRTSTPR",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
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
      "position": 565,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "VFRTSTPRV",
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
            "strain": {
              "Sierra Leone": 3
            },
            "date": {
              "1980": 1,
              "1979": 1,
              "2012": 1
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
      "position": 566,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "FRTSTPRVV",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "strain": {
              "Sierra Leone": 3
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
            "species": {
              "Homo sapiens": 2,
              "Unknown": 1
            }
          }
        }
      ]
    },
    {
      "position": 567,
      "low_support": true,
      "entropy": 0.0,
      "support": 3,
      "distinct_variants_count": 0,
      "distinct_variants_incidence": 0.0,
      "variants": [
        {
          "sequence": "RTSTPRVVL",
          "count": 3,
          "incidence": 100.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "date": {
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "strain": {
              "Sierra Leone": 3
            },
            "accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
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
| -n           | String   | False        | Unknown                     | `dima-cli -i sequences.afa -f "accession\|strain\|country" -n "Unknown"` | Silently fix missing values in the FASTA header with given value.                             |
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
| header_fillna     | String          | False        | Unknown                    | Silently fix missing values in the FASTA header with given value (only required when `header_format` is given). |
| json              | Boolean         | False        | False                      | Whether the result is a JSON string, or a Python object.                                                        |
| header_format     | String          | False        | N/A                        | The format of the FASTA header. Labels where each variant of a kmer position originated from.                   |
| support_threshold | Integer         | False        | 30                         | The minimum required support for each kmer position.                                                            |
| protein_name      | String          | False        | Unknown Protein            | The name of the protein that will appear on the results.                                                        |
| json_save_path    | String          | False        | stdout (prints to console) | The location where the results shall be saved (only required when ```json = True```).                           |
