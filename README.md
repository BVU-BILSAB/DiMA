# DiMA - Diversity Motif Analyser
[![Python package](https://github.com/PU-SDS/DiMA/actions/workflows/python-package.yml/badge.svg)](https://github.com/PU-SDS/DiMA/actions/workflows/python-package.yml)
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
   "low_support":false,
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
   "sequence_count":203,
   "support_threshold":30,
   "low_support":false,
   "protein_name":"Unknown Protein",
   "kmer_length":9,
   "results":[
      {
         "position":1,
         "low_support":false,
         "entropy":0.8361476856397749,
         "support":124,
         "distinct_variants_count":4,
         "distinct_variants_incidence":3.2258062,
         "variants":[
            {
               "sequence":"MKNIIALSY",
               "count":13,
               "incidence":10.4838705,
               "motif_short":"Ma",
               "motif_long":"Major",
               "metadata":{
                  "strain":[
                     "A/India/Pun_1922030/2019",
                     "A/India/Pun_1922292/2019",
                     "A/India/Pun_1921693/2019",
                     "A/India/Pun_1922218/2019",
                     "A/India/Pun_1922278/2019",
                     "A/India/Pun_1924667/2019",
                     "A/India/Pun_1923708/2019",
                     "A/India/Pun_1921994/2019",
                     "A/India/Pun_1922260/2019",
                     "A/India/Pun_1922016/2019",
                     "A/India/Pun_1923690/2019",
                     "A/India/Pun_1922295/2019",
                     "A/India/Pun_1923665/2019"
                  ],
                  "country":[
                     "India",
                     "India",
                     "India",
                     "India",
                     "India",
                     "India",
                     "India",
                     "India",
                     "India",
                     "India",
                     "India",
                     "India",
                     "India"
                  ],
                  "accession":[
                     "MN955496",
                     "MN955492",
                     "MN955499",
                     "MN955502",
                     "MN955493",
                     "MN955488",
                     "MN955487",
                     "MN955498",
                     "MN955494",
                     "MN955497",
                     "MN955489",
                     "MN955491",
                     "MN955490"
                  ],
                  "date":[
                     "08/04/2019",
                     "08/19/2019",
                     "07/17/2019",
                     "08/09/2019",
                     "08/18/2019",
                     "08/01/2019",
                     "09/07/2019",
                     "07/26/2019",
                     "08/16/2019",
                     "07/30/2019",
                     "08/31/2019",
                     "08/20/2019",
                     "09/01/2019"
                  ]
               }
            },
            {
               "sequence":"MKTIIALSY",
               "count":105,
               "incidence":84.67742,
               "motif_short":"I",
               "motif_long":"Index",
               "metadata":{
                  "date":[
                     "01/02/2019",
                     "02/17/2019",
                     "01/14/2019",
                     "02/17/2019",
                     "01/17/2019",
                     "03/14/2019",
                     "02/13/2019",
                     "01/02/2019",
                     "02/06/2019",
                     "01/18/2019",
                     "10/11/2019",
                     "11/15/2019",
                     "01/10/2019",
                     "01/17/2019",
                     "01/17/2019",
                     "01/24/2019",
                     "02/01/2019",
                     "02/01/2019",
                     "02/01/2019",
                     "02/14/2019",
                     "03/14/2019",
                     "07/25/2019",
                     "08/21/2019",
                     "09/05/2019",
                     "09/05/2019",
                     "03/2019",
                     "02/2019",
                     "01/28/2019",
                     "10/08/2019",
                     "03/27/2019",
                     "02/14/2019",
                     "03/14/2019",
                     "01/15/2019",
                     "01/19/2019",
                     "01/28/2019",
                     "01/18/2019",
                     "02/14/2019",
                     "01/04/2019",
                     "01/08/2019",
                     "01/07/2019",
                     "01/28/2019",
                     "01/2019",
                     "01/10/2019",
                     "01/11/2019",
                     "01/13/2019",
                     "01/24/2019",
                     "01/08/2019",
                     "01/09/2019",
                     "01/14/2019",
                     "01/10/2019",
                     "02/2019",
                     "01/2019",
                     "09/05/2019",
                     "01/19/2019",
                     "01/03/2019",
                     "01/23/2019",
                     "02/01/2019",
                     "02/21/2019",
                     "02/28/2019",
                     "02/05/2019",
                     "01/07/2019",
                     "01/08/2019",
                     "01/08/2019",
                     "01/28/2019",
                     "01/28/2019",
                     "01/29/2019",
                     "01/29/2019",
                     "01/29/2019",
                     "01/30/2019",
                     "01/30/2019",
                     "01/30/2019",
                     "01/31/2019",
                     "01/31/2019",
                     "01/31/2019",
                     "01/09/2019",
                     "02/27/2019",
                     "03/05/2019",
                     "03/05/2019",
                     "03/05/2019",
                     "03/05/2019",
                     "03/08/2019",
                     "03/08/2019",
                     "03/04/2019",
                     "03/12/2019",
                     "01/05/2019",
                     "01/28/2019",
                     "01/29/2019",
                     "01/31/2019",
                     "02/22/2019",
                     "03/05/2019",
                     "01/23/2019",
                     "02/19/2019",
                     "04/14/2019",
                     "01/17/2019",
                     "04/04/2019",
                     "02/01/2019",
                     "02/01/2019",
                     "03/21/2019",
                     "05/24/2019",
                     "08/13/2019",
                     "08/05/2019",
                     "01/08/2019",
                     "01/14/2019",
                     "01/21/2019",
                     "01/12/2019"
                  ],
                  "country":[
                     "Iran",
                     "Iran",
                     "Turkey",
                     "Iran",
                     "China",
                     "China",
                     "India",
                     "Iran",
                     "India",
                     "Japan",
                     "China",
                     "China",
                     "China",
                     "China",
                     "China",
                     "China",
                     "China",
                     "China",
                     "China",
                     "China",
                     "China",
                     "China",
                     "China",
                     "China",
                     "China",
                     "China",
                     "China",
                     "Japan",
                     "China",
                     "Japan",
                     "China",
                     "China",
                     "Japan",
                     "Japan",
                     "Japan",
                     "South_Korea",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "China",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "South_Korea",
                     "South_Korea",
                     "South_Korea",
                     "South_Korea",
                     "China",
                     "China",
                     "China",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "South_Korea",
                     "South_Korea",
                     "South_Korea",
                     "South_Korea",
                     "South_Korea",
                     "South_Korea",
                     "South_Korea",
                     "South_Korea",
                     "South_Korea",
                     "South_Korea",
                     "Japan",
                     "Japan",
                     "Japan",
                     "Japan",
                     "South_Korea",
                     "South_Korea",
                     "Japan",
                     "South_Korea",
                     "South_Korea",
                     "Japan",
                     "South_Korea",
                     "China",
                     "China",
                     "China",
                     "India",
                     "India",
                     "India",
                     "South_Korea",
                     "South_Korea",
                     "South_Korea",
                     "South_Korea"
                  ],
                  "accession":[
                     "MK592790",
                     "MK648247",
                     "MK840323",
                     "MK648248",
                     "MT102500",
                     "MT102510",
                     "MK592841",
                     "MK592791",
                     "MK592842",
                     "MK785815",
                     "MT102520",
                     "MT102521",
                     "MT102498",
                     "MT102499",
                     "MT102501",
                     "MT102502",
                     "MT102504",
                     "MT102506",
                     "MT102507",
                     "MT102508",
                     "MT102512",
                     "MT102514",
                     "MT102515",
                     "MT102516",
                     "MT102517",
                     "MN594842",
                     "MN594840",
                     "MK869211",
                     "MT102519",
                     "MN074410",
                     "MT102509",
                     "MT102511",
                     "MK785807",
                     "MK785831",
                     "MK633673",
                     "MK763864",
                     "MN873980",
                     "MK905306",
                     "MK633641",
                     "MK576906",
                     "MK633649",
                     "MN594838",
                     "MK743434",
                     "MK743442",
                     "MK743450",
                     "MK785847",
                     "MK763014",
                     "MK786319",
                     "MK869555",
                     "MK869563",
                     "MN594841",
                     "MN594839",
                     "MT102518",
                     "MK785823",
                     "MK576890",
                     "MK785839",
                     "MK869203",
                     "MK912758",
                     "MK912766",
                     "MK927223",
                     "MK633617",
                     "MK633625",
                     "MK633633",
                     "MK633657",
                     "MK633681",
                     "MK633689",
                     "MK633697",
                     "MK898645",
                     "MK633705",
                     "MK633713",
                     "MK633721",
                     "MK633729",
                     "MK633737",
                     "MK898652",
                     "MK868723",
                     "MK913110",
                     "MK913126",
                     "MK913134",
                     "MK913142",
                     "MK913158",
                     "MK913166",
                     "MK913174",
                     "MK913182",
                     "MN169149",
                     "MK576898",
                     "MK633665",
                     "MK898639",
                     "MK898657",
                     "MK913102",
                     "MK913150",
                     "MK762978",
                     "MK913118",
                     "MN081410",
                     "MK742954",
                     "MN074010",
                     "MT102503",
                     "MT102505",
                     "MT102513",
                     "MN955500",
                     "MN955495",
                     "MN955501",
                     "MK763848",
                     "MK763856",
                     "MK763872",
                     "MK869539"
                  ],
                  "strain":[
                     "A/Alborz/153084/2019",
                     "A/Iran/Clinical_Sample/2019",
                     "A/Turkey/8543/2019",
                     "A/Iran/Clinical_Sample/2019",
                     "A/Homo_sapien/China/LS320/2019",
                     "A/Homo_sapien/China/LS330/2019",
                     "A/India/Pun_19615/2019",
                     "A/Alborz/153427/2019",
                     "A/India/Pun_19533/2019",
                     "A/Japan/8262/2019",
                     "A/Homo_sapien/China/LS340/2019",
                     "A/Homo_sapien/China/LS341/2019",
                     "A/Homo_sapien/China/LS318/2019",
                     "A/Homo_sapien/China/LS319/2019",
                     "A/Homo_sapien/China/LS321/2019",
                     "A/Homo_sapien/China/LS322/2019",
                     "A/Homo_sapien/China/LS324/2019",
                     "A/Homo_sapien/China/LS326/2019",
                     "A/Homo_sapien/China/LS327/2019",
                     "A/Homo_sapien/China/LS328/2019",
                     "A/Homo_sapien/China/LS332/2019",
                     "A/Homo_sapien/China/LS334/2019",
                     "A/Homo_sapien/China/LS335/2019",
                     "A/Homo_sapien/China/LS336/2019",
                     "A/Homo_sapien/China/LS337/2019",
                     "A/Wuhan/11193/2019",
                     "A/Wuhan/1120/2019",
                     "A/Japan/8604/2019",
                     "A/Homo_sapien/China/LS339/2019",
                     "A/Japan/9505/2019",
                     "A/Homo_sapien/China/LS329/2019",
                     "A/Homo_sapien/China/LS331/2019",
                     "A/Japan/8261/2019",
                     "A/Japan/8264/2019",
                     "A/Japan/NHRC_OID_FDX70576/2019",
                     "A/South_Korea/8207/2019",
                     "A/Yokosuka/NHRC_OID_FDX70622/2019",
                     "A/Japan/NHRC_OID_FDX70557/2019",
                     "A/Japan/NHRC_OID_FDX70566/2019",
                     "A/Japan/7848/2019",
                     "A/Japan/NHRC_OID_FDX70571/2019",
                     "A/Wuhan/345/2019",
                     "A/Japan/8000/2019",
                     "A/Japan/8001/2019",
                     "A/Japan/8002/2019",
                     "A/Japan/8266/2019",
                     "A/South_Korea/8203/2019",
                     "A/South_Korea/8352/2019",
                     "A/South_Korea/8671/2019",
                     "A/South_Korea/8674/2019",
                     "A/Wuhan/5413/2019",
                     "A/Wuhan/877/2019",
                     "A/Homo_sapien/China/LS338/2019",
                     "A/Japan/8263/2019",
                     "A/Japan/7846/2019",
                     "A/Japan/8265/2019",
                     "A/Japan/8603/2019",
                     "A/Japan/8768/2019",
                     "A/Japan/8769/2019",
                     "A/Japan/8957/2019",
                     "A/Japan/NHRC_OID_FDX70561/2019",
                     "A/Japan/NHRC_OID_FDX70563/2019",
                     "A/Japan/NHRC_OID_FDX70564/2019",
                     "A/Japan/NHRC_OID_FDX70572/2019",
                     "A/Japan/NHRC_OID_FDX70577/2019",
                     "A/Japan/NHRC_OID_FDX70579/2019",
                     "A/Japan/NHRC_OID_FDX70583/2019",
                     "A/Japan/NHRC_OID_FDX70584/2019",
                     "A/Japan/NHRC_OID_FDX70586/2019",
                     "A/Japan/NHRC_OID_FDX70587/2019",
                     "A/Japan/NHRC_OID_FDX70589/2019",
                     "A/Japan/NHRC_OID_FDX70590/2019",
                     "A/Japan/NHRC_OID_FDX70591/2019",
                     "A/Japan/NHRC_OID_FDX70592/2019",
                     "A/South_Korea/8667/2019",
                     "A/South_Korea/8823/2019",
                     "A/South_Korea/8825/2019",
                     "A/South_Korea/8826/2019",
                     "A/South_Korea/8827/2019",
                     "A/South_Korea/8829/2019",
                     "A/South_Korea/8830/2019",
                     "A/South_Korea/8831/2019",
                     "A/South_Korea/8832/2019",
                     "A/South_Korea/9116/2019",
                     "A/Japan/7847/2019",
                     "A/Japan/NHRC_OID_FDX70574/2019",
                     "A/Japan/NHRC_OID_FDX70581/2019",
                     "A/Japan/NHRC_OID_FDX70593/2019",
                     "A/South_Korea/8822/2019",
                     "A/South_Korea/8828/2019",
                     "A/Japan/8142/2019",
                     "A/South_Korea/8824/2019",
                     "A/South_Korea/9704/2019",
                     "A/Japan/8003/2019",
                     "A/South_Korea/9578/2019",
                     "A/Homo_sapien/China/LS323/2019",
                     "A/Homo_sapien/China/LS325/2019",
                     "A/Homo_sapien/China/LS333/2019",
                     "A/India/Pun_1920970/2019",
                     "A/India/Pun_1922253/2019",
                     "A/India/Pun_1922052/2019",
                     "A/South_Korea/8204/2019",
                     "A/South_Korea/8206/2019",
                     "A/South_Korea/8208/2019",
                     "A/South_Korea/8668/2019"
                  ]
               }
            },
            {
               "sequence":"MKTIIALSC",
               "count":2,
               "incidence":1.6129031,
               "motif_short":"Mi",
               "motif_long":"Minor",
               "metadata":{
                  "accession":[
                     "MN169648",
                     "MN873990"
                  ],
                  "country":[
                     "Japan",
                     "Japan"
                  ],
                  "strain":[
                     "A/Japan/9070/2019",
                     "A/Yokosuka/NHRC_OID_FDX70722/2019"
                  ],
                  "date":[
                     "03/12/2019",
                     "04/17/2019"
                  ]
               }
            },
            {
               "sequence":"METISLISM",
               "count":1,
               "incidence":0.80645156,
               "motif_short":"U",
               "motif_long":"Unique",
               "metadata":{
                  "accession":[
                     "MN853423"
                  ],
                  "country":[
                     "China"
                  ],
                  "strain":[
                     "A/Beijing/16/2019"
                  ],
                  "date":[
                     "01/2019"
                  ]
               }
            },
            {
               "sequence":"MKTIIALSH",
               "count":3,
               "incidence":2.4193547,
               "motif_short":"Mi",
               "motif_long":"Minor",
               "metadata":{
                  "country":[
                     "South_Korea",
                     "South_Korea",
                     "South_Korea"
                  ],
                  "date":[
                     "04/05/2019",
                     "04/10/2019",
                     "04/11/2019"
                  ],
                  "strain":[
                     "A/South_Korea/9579/2019",
                     "A/South_Korea/9645/2019",
                     "A/South_Korea/9646/2019"
                  ],
                  "accession":[
                     "MN074938",
                     "MN078683",
                     "MN078691"
                  ]
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
| -n           | String   | False        | N/A (raise error)           | `dima-cli -i sequences.afa -f "accession/|strain/|country" -n "Unknown"` | Silently fix missing values in the FASTA header with given value.                             |
| -v           | N/A      | False        | N/A                         | `dima-cli -v`                                                            | Prints the version of dima-cli that is currently installed.                                   |
| -p           | String   | False        | Unknown Protein             | `dima-cli -n "Coronavirus Surface Protein" -i sequences.afa`             | The name of the protein that will appear on the results.                                      |
| -i           | String   | True         | N/A                         | `dima-cli -i sequences.afa`                                              | The path to the FASTA Multiple Sequence Alignment file.                                       |
| -o           | String   | False        | stdout (prints the results) | `dima-cli -i sequences.afa -o results,json`                              | The location where the results shall be saved.                                                |
| -l           | Integer  | False        | 9                           | `dima-cli -i sequences.afa -l 12`                                        | The length of the kmers generated.                                                            |
| -f           | String   | False        | N/A                         | `dima-cli -i sequences.afa -f "accession/|strain/|country"`              | The format of the FASTA header. Labels where each variant of a kmer position originated from. |
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
| json_save_path    | String          | False        | STDOUT (prints to console) | The location where the results shall be saved (only required when ```json = True```).                           |
