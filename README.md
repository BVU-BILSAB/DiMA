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
<details>
<summary>Click to view basic results</summary>

```
{
  "sequence_count": 5,
  "support_threshold": 30,
  "low_support_count": 20,
  "query_name": "Unknown Query",
  "kmer_length": 9,
  "results": [
    {
      "position": 1,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "MSASKEIKS",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": null
        },
        {
          "sequence": "SAGVYMGNL",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        }
      ]
    },
    {
      "position": 2,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "AGVYMGNLS",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        },
        {
          "sequence": "SASKEIKSF",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": null
        }
      ]
    },
    {
      "position": 3,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "GVYMGNLSS",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        },
        {
          "sequence": "ASKEIKSFL",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": null
        }
      ]
    },
    {
      "position": 4,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "VYMGNLSSQ",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        },
        {
          "sequence": "SKEIKSFLW",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": null
        }
      ]
    },
    {
      "position": 5,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "KEIKSFLWT",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": null
        },
        {
          "sequence": "YMGNLSSQQ",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        }
      ]
    },
    {
      "position": 6,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "MGNLSSQQL",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        },
        {
          "sequence": "EIKSFLWTQ",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": null
        }
      ]
    },
    {
      "position": 7,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "IKSFLWTQS",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": null
        },
        {
          "sequence": "GNLSSQQLD",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        }
      ]
    },
    {
      "position": 8,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "KSFLWTQSL",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": null
        },
        {
          "sequence": "NLSSQQLDQ",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        }
      ]
    },
    {
      "position": 9,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "SFLWTQSLR",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": null
        },
        {
          "sequence": "LSSQQLDQR",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        }
      ]
    },
    {
      "position": 10,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "SSQQLDQRR",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        },
        {
          "sequence": "FLWTQSLRR",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": null
        }
      ]
    },
    {
      "position": 11,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "LWTQSLRRE",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": null
        },
        {
          "sequence": "SQQLDQRRA",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        }
      ]
    },
    {
      "position": 12,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "QQLDQRRAL",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        },
        {
          "sequence": "WTQSLRREL",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": null
        }
      ]
    },
    {
      "position": 13,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "TQSLRRELS",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": null
        },
        {
          "sequence": "QLDQRRALL",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        }
      ]
    },
    {
      "position": 14,
      "low_support": "LS",
      "entropy": 1.3709505944546687,
      "support": 5,
      "distinct_variants_count": 2,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 40.0,
      "diversity_motifs": [
        {
          "sequence": "QSLRRELSG",
          "count": 3,
          "incidence": 60.000004,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": null
        },
        {
          "sequence": "LDQRRALLS",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        },
        {
          "sequence": "QSLRRELSS",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        }
      ]
    },
    {
      "position": 15,
      "low_support": "LS",
      "entropy": 1.3709505944546687,
      "support": 5,
      "distinct_variants_count": 2,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 40.0,
      "diversity_motifs": [
        {
          "sequence": "DQRRALLSM",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        },
        {
          "sequence": "SLRRELSGY",
          "count": 3,
          "incidence": 60.000004,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": null
        },
        {
          "sequence": "SLRRELSSY",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        }
      ]
    },
    {
      "position": 16,
      "low_support": "LS",
      "entropy": 1.3709505944546687,
      "support": 5,
      "distinct_variants_count": 2,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 40.0,
      "diversity_motifs": [
        {
          "sequence": "QRRALLSMI",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        },
        {
          "sequence": "LRRELSSYC",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        },
        {
          "sequence": "LRRELSGYC",
          "count": 3,
          "incidence": 60.000004,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": null
        }
      ]
    },
    {
      "position": 17,
      "low_support": "LS",
      "entropy": 1.3709505944546687,
      "support": 5,
      "distinct_variants_count": 2,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 40.0,
      "diversity_motifs": [
        {
          "sequence": "RRELSGYCS",
          "count": 3,
          "incidence": 60.000004,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": null
        },
        {
          "sequence": "RRALLSMIG",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        },
        {
          "sequence": "RRELSSYCS",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        }
      ]
    },
    {
      "position": 18,
      "low_support": "LS",
      "entropy": 1.3709505944546687,
      "support": 5,
      "distinct_variants_count": 2,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 40.0,
      "diversity_motifs": [
        {
          "sequence": "RELSGYCSN",
          "count": 3,
          "incidence": 60.000004,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": null
        },
        {
          "sequence": "RALLSMIGM",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        },
        {
          "sequence": "RELSSYCSN",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        }
      ]
    },
    {
      "position": 19,
      "low_support": "LS",
      "entropy": 1.3709505944546687,
      "support": 5,
      "distinct_variants_count": 2,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 40.0,
      "diversity_motifs": [
        {
          "sequence": "ALLSMIGMS",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        },
        {
          "sequence": "ELSSYCSNI",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        },
        {
          "sequence": "ELSGYCSNI",
          "count": 3,
          "incidence": 60.000004,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": null
        }
      ]
    },
    {
      "position": 20,
      "low_support": "LS",
      "entropy": 1.3709505944546687,
      "support": 5,
      "distinct_variants_count": 2,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 40.0,
      "diversity_motifs": [
        {
          "sequence": "LSGYCSNIK",
          "count": 3,
          "incidence": 60.000004,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": null
        },
        {
          "sequence": "LLSMIGMSG",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        },
        {
          "sequence": "LSSYCSNIK",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": null
        }
      ]
    }
  ]
}
```
</details>

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
<details>
<summary>Click to view advanced results</summary>

```
{
  "sequence_count": 5,
  "support_threshold": 30,
  "low_support_count": 20,
  "query_name": "Unknown Query",
  "kmer_length": 9,
  "results": [
    {
      "position": 1,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "MSASKEIKS",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "Accession": {
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75321.1": 1,
              "AYD75325.1": 1
            },
            "Country": {
              "Sierra Leone": 4
            },
            "Species": {
              "Homo sapiens": 3,
              "Unknown": 1
            },
            "Year": {
              "1977": 1,
              "2012": 1,
              "1980": 1,
              "1979": 1
            }
          }
        },
        {
          "sequence": "SAGVYMGNL",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Accession": {
              "AYD75329.1": 1
            },
            "Country": {
              "Sierra Leone": 1
            },
            "Year": {
              "1975": 1
            },
            "Species": {
              "Homo sapiens": 1
            }
          }
        }
      ]
    },
    {
      "position": 2,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "SASKEIKSF",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "Species": {
              "Homo sapiens": 3,
              "Unknown": 1
            },
            "Year": {
              "1977": 1,
              "1980": 1,
              "1979": 1,
              "2012": 1
            },
            "Country": {
              "Sierra Leone": 4
            },
            "Accession": {
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75321.1": 1
            }
          }
        },
        {
          "sequence": "AGVYMGNLS",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Species": {
              "Homo sapiens": 1
            },
            "Year": {
              "1975": 1
            },
            "Accession": {
              "AYD75329.1": 1
            },
            "Country": {
              "Sierra Leone": 1
            }
          }
        }
      ]
    },
    {
      "position": 3,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "ASKEIKSFL",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "Year": {
              "1980": 1,
              "1977": 1,
              "1979": 1,
              "2012": 1
            },
            "Accession": {
              "AYD75321.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "Country": {
              "Sierra Leone": 4
            },
            "Species": {
              "Unknown": 1,
              "Homo sapiens": 3
            }
          }
        },
        {
          "sequence": "GVYMGNLSS",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Accession": {
              "AYD75329.1": 1
            },
            "Species": {
              "Homo sapiens": 1
            },
            "Country": {
              "Sierra Leone": 1
            },
            "Year": {
              "1975": 1
            }
          }
        }
      ]
    },
    {
      "position": 4,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "SKEIKSFLW",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "Accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1,
              "AYD75321.1": 1
            },
            "Country": {
              "Sierra Leone": 4
            },
            "Species": {
              "Unknown": 1,
              "Homo sapiens": 3
            },
            "Year": {
              "2012": 1,
              "1979": 1,
              "1980": 1,
              "1977": 1
            }
          }
        },
        {
          "sequence": "VYMGNLSSQ",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Accession": {
              "AYD75329.1": 1
            },
            "Year": {
              "1975": 1
            },
            "Species": {
              "Homo sapiens": 1
            },
            "Country": {
              "Sierra Leone": 1
            }
          }
        }
      ]
    },
    {
      "position": 5,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "KEIKSFLWT",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "Accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75321.1": 1,
              "AYD75365.1": 1
            },
            "Year": {
              "1979": 1,
              "1980": 1,
              "1977": 1,
              "2012": 1
            },
            "Country": {
              "Sierra Leone": 4
            },
            "Species": {
              "Homo sapiens": 3,
              "Unknown": 1
            }
          }
        },
        {
          "sequence": "YMGNLSSQQ",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Country": {
              "Sierra Leone": 1
            },
            "Year": {
              "1975": 1
            },
            "Species": {
              "Homo sapiens": 1
            },
            "Accession": {
              "AYD75329.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 6,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "MGNLSSQQL",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Accession": {
              "AYD75329.1": 1
            },
            "Country": {
              "Sierra Leone": 1
            },
            "Species": {
              "Homo sapiens": 1
            },
            "Year": {
              "1975": 1
            }
          }
        },
        {
          "sequence": "EIKSFLWTQ",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "Accession": {
              "AYD75321.1": 1,
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1
            },
            "Species": {
              "Unknown": 1,
              "Homo sapiens": 3
            },
            "Country": {
              "Sierra Leone": 4
            },
            "Year": {
              "1977": 1,
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
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "GNLSSQQLD",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Country": {
              "Sierra Leone": 1
            },
            "Species": {
              "Homo sapiens": 1
            },
            "Accession": {
              "AYD75329.1": 1
            },
            "Year": {
              "1975": 1
            }
          }
        },
        {
          "sequence": "IKSFLWTQS",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "Accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "QEP52131.1": 1,
              "AYD75321.1": 1
            },
            "Year": {
              "1979": 1,
              "1980": 1,
              "1977": 1,
              "2012": 1
            },
            "Species": {
              "Unknown": 1,
              "Homo sapiens": 3
            },
            "Country": {
              "Sierra Leone": 4
            }
          }
        }
      ]
    },
    {
      "position": 8,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "NLSSQQLDQ",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Country": {
              "Sierra Leone": 1
            },
            "Year": {
              "1975": 1
            },
            "Species": {
              "Homo sapiens": 1
            },
            "Accession": {
              "AYD75329.1": 1
            }
          }
        },
        {
          "sequence": "KSFLWTQSL",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "Country": {
              "Sierra Leone": 4
            },
            "Year": {
              "1979": 1,
              "2012": 1,
              "1977": 1,
              "1980": 1
            },
            "Species": {
              "Unknown": 1,
              "Homo sapiens": 3
            },
            "Accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "AYD75321.1": 1,
              "QEP52131.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 9,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "SFLWTQSLR",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "Year": {
              "2012": 1,
              "1979": 1,
              "1980": 1,
              "1977": 1
            },
            "Accession": {
              "QEP52131.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "AYD75321.1": 1
            },
            "Country": {
              "Sierra Leone": 4
            },
            "Species": {
              "Unknown": 1,
              "Homo sapiens": 3
            }
          }
        },
        {
          "sequence": "LSSQQLDQR",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Species": {
              "Homo sapiens": 1
            },
            "Accession": {
              "AYD75329.1": 1
            },
            "Year": {
              "1975": 1
            },
            "Country": {
              "Sierra Leone": 1
            }
          }
        }
      ]
    },
    {
      "position": 10,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "FLWTQSLRR",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "Year": {
              "1977": 1,
              "2012": 1,
              "1980": 1,
              "1979": 1
            },
            "Accession": {
              "AYD75321.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "QEP52131.1": 1
            },
            "Species": {
              "Unknown": 1,
              "Homo sapiens": 3
            },
            "Country": {
              "Sierra Leone": 4
            }
          }
        },
        {
          "sequence": "SSQQLDQRR",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Species": {
              "Homo sapiens": 1
            },
            "Year": {
              "1975": 1
            },
            "Accession": {
              "AYD75329.1": 1
            },
            "Country": {
              "Sierra Leone": 1
            }
          }
        }
      ]
    },
    {
      "position": 11,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "LWTQSLRRE",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "Country": {
              "Sierra Leone": 4
            },
            "Accession": {
              "QEP52131.1": 1,
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "AYD75321.1": 1
            },
            "Species": {
              "Homo sapiens": 3,
              "Unknown": 1
            },
            "Year": {
              "1979": 1,
              "1980": 1,
              "2012": 1,
              "1977": 1
            }
          }
        },
        {
          "sequence": "SQQLDQRRA",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Accession": {
              "AYD75329.1": 1
            },
            "Species": {
              "Homo sapiens": 1
            },
            "Country": {
              "Sierra Leone": 1
            },
            "Year": {
              "1975": 1
            }
          }
        }
      ]
    },
    {
      "position": 12,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "QQLDQRRAL",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Country": {
              "Sierra Leone": 1
            },
            "Species": {
              "Homo sapiens": 1
            },
            "Year": {
              "1975": 1
            },
            "Accession": {
              "AYD75329.1": 1
            }
          }
        },
        {
          "sequence": "WTQSLRREL",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "Country": {
              "Sierra Leone": 4
            },
            "Year": {
              "1980": 1,
              "2012": 1,
              "1979": 1,
              "1977": 1
            },
            "Accession": {
              "QEP52131.1": 1,
              "AYD75321.1": 1,
              "AYD75325.1": 1,
              "AYD75365.1": 1
            },
            "Species": {
              "Homo sapiens": 3,
              "Unknown": 1
            }
          }
        }
      ]
    },
    {
      "position": 13,
      "low_support": "LS",
      "entropy": 0.7219280948873623,
      "support": 5,
      "distinct_variants_count": 1,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 20.0,
      "diversity_motifs": [
        {
          "sequence": "TQSLRRELS",
          "count": 4,
          "incidence": 80.0,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "Accession": {
              "AYD75365.1": 1,
              "AYD75321.1": 1,
              "QEP52131.1": 1,
              "AYD75325.1": 1
            },
            "Country": {
              "Sierra Leone": 4
            },
            "Year": {
              "1977": 1,
              "1979": 1,
              "2012": 1,
              "1980": 1
            },
            "Species": {
              "Unknown": 1,
              "Homo sapiens": 3
            }
          }
        },
        {
          "sequence": "QLDQRRALL",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Year": {
              "1975": 1
            },
            "Accession": {
              "AYD75329.1": 1
            },
            "Country": {
              "Sierra Leone": 1
            },
            "Species": {
              "Homo sapiens": 1
            }
          }
        }
      ]
    },
    {
      "position": 14,
      "low_support": "LS",
      "entropy": 1.3709505944546687,
      "support": 5,
      "distinct_variants_count": 2,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 40.0,
      "diversity_motifs": [
        {
          "sequence": "QSLRRELSG",
          "count": 3,
          "incidence": 60.000004,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "Country": {
              "Sierra Leone": 3
            },
            "Accession": {
              "AYD75325.1": 1,
              "AYD75321.1": 1,
              "AYD75365.1": 1
            },
            "Species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "Year": {
              "1979": 1,
              "1980": 1,
              "1977": 1
            }
          }
        },
        {
          "sequence": "QSLRRELSS",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Country": {
              "Sierra Leone": 1
            },
            "Year": {
              "2012": 1
            },
            "Species": {
              "Homo sapiens": 1
            },
            "Accession": {
              "QEP52131.1": 1
            }
          }
        },
        {
          "sequence": "LDQRRALLS",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Country": {
              "Sierra Leone": 1
            },
            "Species": {
              "Homo sapiens": 1
            },
            "Accession": {
              "AYD75329.1": 1
            },
            "Year": {
              "1975": 1
            }
          }
        }
      ]
    },
    {
      "position": 15,
      "low_support": "LS",
      "entropy": 1.3709505944546687,
      "support": 5,
      "distinct_variants_count": 2,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 40.0,
      "diversity_motifs": [
        {
          "sequence": "DQRRALLSM",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Country": {
              "Sierra Leone": 1
            },
            "Accession": {
              "AYD75329.1": 1
            },
            "Species": {
              "Homo sapiens": 1
            },
            "Year": {
              "1975": 1
            }
          }
        },
        {
          "sequence": "SLRRELSSY",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Accession": {
              "QEP52131.1": 1
            },
            "Country": {
              "Sierra Leone": 1
            },
            "Species": {
              "Homo sapiens": 1
            },
            "Year": {
              "2012": 1
            }
          }
        },
        {
          "sequence": "SLRRELSGY",
          "count": 3,
          "incidence": 60.000004,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "Species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "Year": {
              "1977": 1,
              "1980": 1,
              "1979": 1
            },
            "Country": {
              "Sierra Leone": 3
            },
            "Accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "AYD75321.1": 1
            }
          }
        }
      ]
    },
    {
      "position": 16,
      "low_support": "LS",
      "entropy": 1.3709505944546687,
      "support": 5,
      "distinct_variants_count": 2,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 40.0,
      "diversity_motifs": [
        {
          "sequence": "LRRELSSYC",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Country": {
              "Sierra Leone": 1
            },
            "Accession": {
              "QEP52131.1": 1
            },
            "Year": {
              "2012": 1
            },
            "Species": {
              "Homo sapiens": 1
            }
          }
        },
        {
          "sequence": "LRRELSGYC",
          "count": 3,
          "incidence": 60.000004,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "Year": {
              "1979": 1,
              "1977": 1,
              "1980": 1
            },
            "Species": {
              "Unknown": 1,
              "Homo sapiens": 2
            },
            "Country": {
              "Sierra Leone": 3
            },
            "Accession": {
              "AYD75365.1": 1,
              "AYD75321.1": 1,
              "AYD75325.1": 1
            }
          }
        },
        {
          "sequence": "QRRALLSMI",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Species": {
              "Homo sapiens": 1
            },
            "Country": {
              "Sierra Leone": 1
            },
            "Accession": {
              "AYD75329.1": 1
            },
            "Year": {
              "1975": 1
            }
          }
        }
      ]
    },
    {
      "position": 17,
      "low_support": "LS",
      "entropy": 1.3709505944546687,
      "support": 5,
      "distinct_variants_count": 2,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 40.0,
      "diversity_motifs": [
        {
          "sequence": "RRELSSYCS",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Year": {
              "2012": 1
            },
            "Accession": {
              "QEP52131.1": 1
            },
            "Country": {
              "Sierra Leone": 1
            },
            "Species": {
              "Homo sapiens": 1
            }
          }
        },
        {
          "sequence": "RRELSGYCS",
          "count": 3,
          "incidence": 60.000004,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "Species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "Year": {
              "1980": 1,
              "1977": 1,
              "1979": 1
            },
            "Accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "AYD75321.1": 1
            },
            "Country": {
              "Sierra Leone": 3
            }
          }
        },
        {
          "sequence": "RRALLSMIG",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Country": {
              "Sierra Leone": 1
            },
            "Species": {
              "Homo sapiens": 1
            },
            "Accession": {
              "AYD75329.1": 1
            },
            "Year": {
              "1975": 1
            }
          }
        }
      ]
    },
    {
      "position": 18,
      "low_support": "LS",
      "entropy": 1.3709505944546687,
      "support": 5,
      "distinct_variants_count": 2,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 40.0,
      "diversity_motifs": [
        {
          "sequence": "RALLSMIGM",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Year": {
              "1975": 1
            },
            "Accession": {
              "AYD75329.1": 1
            },
            "Country": {
              "Sierra Leone": 1
            },
            "Species": {
              "Homo sapiens": 1
            }
          }
        },
        {
          "sequence": "RELSSYCSN",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Species": {
              "Homo sapiens": 1
            },
            "Accession": {
              "QEP52131.1": 1
            },
            "Country": {
              "Sierra Leone": 1
            },
            "Year": {
              "2012": 1
            }
          }
        },
        {
          "sequence": "RELSGYCSN",
          "count": 3,
          "incidence": 60.000004,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "Accession": {
              "AYD75325.1": 1,
              "AYD75365.1": 1,
              "AYD75321.1": 1
            },
            "Species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "Year": {
              "1980": 1,
              "1977": 1,
              "1979": 1
            },
            "Country": {
              "Sierra Leone": 3
            }
          }
        }
      ]
    },
    {
      "position": 19,
      "low_support": "LS",
      "entropy": 1.3709505944546687,
      "support": 5,
      "distinct_variants_count": 2,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 40.0,
      "diversity_motifs": [
        {
          "sequence": "ELSGYCSNI",
          "count": 3,
          "incidence": 60.000004,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "Country": {
              "Sierra Leone": 3
            },
            "Species": {
              "Homo sapiens": 2,
              "Unknown": 1
            },
            "Accession": {
              "AYD75365.1": 1,
              "AYD75325.1": 1,
              "AYD75321.1": 1
            },
            "Year": {
              "1977": 1,
              "1979": 1,
              "1980": 1
            }
          }
        },
        {
          "sequence": "ELSSYCSNI",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Accession": {
              "QEP52131.1": 1
            },
            "Species": {
              "Homo sapiens": 1
            },
            "Country": {
              "Sierra Leone": 1
            },
            "Year": {
              "2012": 1
            }
          }
        },
        {
          "sequence": "ALLSMIGMS",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Country": {
              "Sierra Leone": 1
            },
            "Accession": {
              "AYD75329.1": 1
            },
            "Species": {
              "Homo sapiens": 1
            },
            "Year": {
              "1975": 1
            }
          }
        }
      ]
    },
    {
      "position": 20,
      "low_support": "LS",
      "entropy": 1.3709505944546687,
      "support": 5,
      "distinct_variants_count": 2,
      "distinct_variants_incidence": 100.0,
      "total_variants_incidence": 40.0,
      "diversity_motifs": [
        {
          "sequence": "LLSMIGMSG",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Accession": {
              "AYD75329.1": 1
            },
            "Country": {
              "Sierra Leone": 1
            },
            "Species": {
              "Homo sapiens": 1
            },
            "Year": {
              "1975": 1
            }
          }
        },
        {
          "sequence": "LSGYCSNIK",
          "count": 3,
          "incidence": 60.000004,
          "motif_short": "I",
          "motif_long": "Index",
          "metadata": {
            "Country": {
              "Sierra Leone": 3
            },
            "Year": {
              "1979": 1,
              "1977": 1,
              "1980": 1
            },
            "Accession": {
              "AYD75365.1": 1,
              "AYD75321.1": 1,
              "AYD75325.1": 1
            },
            "Species": {
              "Unknown": 1,
              "Homo sapiens": 2
            }
          }
        },
        {
          "sequence": "LSSYCSNIK",
          "count": 1,
          "incidence": 20.0,
          "motif_short": "U",
          "motif_long": "Unique",
          "metadata": {
            "Year": {
              "2012": 1
            },
            "Species": {
              "Homo sapiens": 1
            },
            "Accession": {
              "QEP52131.1": 1
            },
            "Country": {
              "Sierra Leone": 1
            }
          }
        }
      ]
    }
  ]
}
```
</details>

## Command-Line Arguments
| **Argument** | **Type**           | **Required** | **Default**   | **Example**                                                                                      | **Description**                                                                               |
|--------------|--------------------|--------------|---------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| -h           | N/A                | False        | N/A           | `dima-cli -h`                                                                                    | Prints a summary of all available command-line arguments.                                     |
| -n           | String             | False        | Unknown       | `dima-cli -i sequences.afa -o results.json -f "accession\|strain\|country" -n "NA"` -n "Unknown" | Silently fix missing values in the FASTA header with given value.                             |
| -v           | N/A                | False        | N/A           | `dima-cli -v`                                                                                    | Prints the version of dima-cli that is currently installed.                                   |
| -q           | String             | False        | Unknown Query | `dima-cli -q "Coronavirus Surface Protein" -i sequences.afa -o results.json`                     | The name of the sample that will appear on the results.                                       |
| -i           | String             | True         | N/A           | `dima-cli -i sequences.afa -o results.json`                                                      | The path to the FASTA Multiple Sequence Alignment file.                                       |
| -o           | String             | True         | N/A           | `dima-cli -i sequences.afa -o results,json`                                                      | The location where the results shall be saved.                                                |
| -l           | Integer            | False        | 9             | `dima-cli -i sequences.afa -l 12 -o results.json`                                                | The length of the kmers generated.                                                            |
| -f           | String             | False        | N/A           | `dima-cli -i sequences.afa -f "accession\|strain\|country" -o results.json`                      | The format of the FASTA header. Labels where each variant of a kmer position originated from. |
| -s           | Integer            | False        | 30            | `dima-cli -i sequences.afa -l 12 -s 40  -o results.json`                                         | The minimum required support for each kmer position.                                          |
| -a           | nucleotide/protein | False        | protein       | `dima-cli -i dna_sequences.afa -a nucleotide -o results.json`                                    | The alphabet of the sequences (ie: `protein`/`nucleotide`, default: protein)                  |
| -t           | json/xlsx          | False        | json          | `dima-cli -i dna_sequences.afa -a nucleotide -o results.json -t xlsx`                            | The output format (ie: `json`/`xlsx`, default: json)                                          |
| -c           | String             | False        | N/A           | `dima-cli -i dna_sequences.afa -a nucleotide -o results.json -c hcs.json`                        | Path to save Highly Conserved Sequences (HCS) in JSON format.                                 |
| -e           | Float              | False        | 100           | `dima-cli -i dna_sequences.afa -a nucleotide -o results.json -c hcs.json -e 90.5`                | Minimum incidence (%) threshold for HCS concatenation.                                        |


## Module Parameters
| **Parameter**     | **Type**        | **Required** | **Default**     | **Description**                                                                                                 |
|-------------------|-----------------|--------------|-----------------|-----------------------------------------------------------------------------------------------------------------|
| sequences         | String/StringIO | True         | N/A             | The path to a FASTA Multiple Sequence Alignment file (MSA), or a StringIO object containing FASTA MSA.          |
| kmer_length       | Integer         | False        | 9               | The length of the kmers generated.                                                                              |
| header_fillna     | String          | False        | Unknown         | Silently fix missing values in the FASTA header with given value (only required when `header_format` is given). |
| header_format     | String          | False        | N/A             | The format of the FASTA header. Labels where each variant of a kmer position originated from.                   |
| support_threshold | Integer         | False        | 30              | The minimum required support for each kmer position.                                                            |
| query_name        | String          | False        | Unknown Query   | The name of the sample that will appear on the results.                                                         |
| alphabet          | String          | False        | protein         | The alphabet of the sequences (ie: protein/nucleotide, default: protein)                                        |
