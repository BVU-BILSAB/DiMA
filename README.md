# Hunana

A modular implementation of Hunana. A sub-module of ViVA.

The conserved sequences of the viral protein sequences are considered as candidates for vaccine design against 
continuously mutating viruses. Nonameric sequences from the viral genome are recognized and processed by human leukocyte 
antigens and T cell receptors. HUNANA is a command-line based tool which can provide a list of positions of conserved 
nonameric (kmer) sequences for a given viral protein sequence by utilizing Shannon’s entropy formula.  

## Installation

**OPTION 1**

`pip install hunana`

**OPTION 2**

`pip install git+https://github.com/pu-sds/hunana.git`

**OPTION 3**

```
git clone https://github.com/pu-sds/hunana.git
cd hunana
python setup.py install
```

**OPTION 4**

Download the latest distribution at:

`https://github.com/pu-sds/hunana/releases/latest`

Install using:

`$ pip install hunana-{version}.whl`

### Command-Line Usage
Once installation is complete, an executable will be added to PATH which can be accessed as below:

**Linux**

`hunana -h`

**Windows**

`hunana.exe -h`

#### Basic Usage
`hunana -i sequences.fasta -o output.json -l 9`

`hunana -i sequences.fasta | grep supports`

##### Basic Usage Output (Example)
```
[
  {
    "position":1,
    "entropy":1.0002713744986218,
    "supports":2,
    "variants":[
      {
        "position":1,
        "sequence":"SKGKRTVDL",
        "count":1,
        "incidence":50.0,
        "motif_short":"I",
        "motif_long":"Index"
      },
      {
        "position":1,
        "sequence":"FHWLMLNPN",
        "count":1,
        "incidence":50.0,
        "motif_short":"Ma",
        "motif_long":"Major"
      }
    ],
    "kmer_types":{
      "incidence":50.0,
      "types":[
        "FHWLMLNPN"
      ]
    }
  }
]
```

#### Advanced Usage (Generate Variant Data)
The flag --he/--header along with the -f/--format header can be used to generate data for each variant using the metadata from the fasta sequence header.

`hunana -i sequences.fasta -o output.json -he -f "(type)|(id)|(strain)"`

Each componant (ex: id, strain, country, etc)of the header needs to be wrapped in brackets. Any separator (Ex: |, /, _, etc) can be used.

##### Advanced Usage Output (Example)
```
[
  {
    "position":1,
    "entropy":1.0001724373828909,
    "supports":2,
    "variants":[
      {
        "position":1,
        "sequence":"SKGKRTVDL",
        "count":1,
        "incidence":50.0,
        "motif_short":"I",
        "motif_long":"Index",
        "type":[
          "tr"
        ],
        "accession":[
          "A0A2Z4MTJ4"
        ],
        "strain":[
          "A0A2Z4MTJ4_9HIV2_Envelope_glycoprotein_gp160_OS_Human_immunodeficiency_virus_2_OX_11709_GN_env_PE_4_SV_1"
        ]
      },
      {
        "position":1,
        "sequence":"FHWLMLNPN",
        "count":1,
        "incidence":50.0,
        "motif_short":"Ma",
        "motif_long":"Major",
        "type":[
          "tr"
        ],
        "accession":[
          "A0A0K2GVL2"
        ],
        "strain":[
          "A0A2Z4MTJ4_9HIV2_Envelope_glycoprotein_gp160_OS_Human_immunodeficiency_virus_2_OX_11709_GN_env_PE_4_SV_1"
        ]
      }
    ],
    "kmer_types":{
      "incidence":50.0,
      "types":[
        "FHWLMLNPN"
      ]
    }
  }
]
```

#### Command-Line Arguments
```
usage: hunana [-h] -i INPUT -o OUTPUT [-l {1,2,3,4,5,6,7,8,9,10,11,12,13,14}]
              [-s SAMPLES] [-it ITERATIONS] [-he] [-f FORMAT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Absolute path to the aligned sequences file in FASTA
                        format.
  -o OUTPUT, --output OUTPUT
                        Absolute path to the output file.
  -l {1,2,3,4,5,6,7,8,9,10,11,12,13,14}, --length {1,2,3,4,5,6,7,8,9,10,11,12,13,14}
                        The k-mer length (default: 9).
  -s SAMPLES, --samples SAMPLES
                        Max number of samples use when calculating entropy
                        (default: 10000).
  -it ITERATIONS, --iterations ITERATIONS
                        Max number of iterations used when calculating entropy
                        (default: 10).
  -he, --header         Should the header data be used to derive the details
                        for variants?.
  -f FORMAT, --format FORMAT
                        The format of the header. Ex:
                        "(id)|(species)|(country)". Each item enclosed in
                        brackets with any character used as separator.
```

#### More Examples
`hunana -i sequences.fasta -o output.json -he -f "(ncbid)/(strain)/(host)/(country)"`

`hunana -i sequences.fasta -o output.json -he -f "(ncbid)/(strain)/(host)|(country)"`

`hunana -i sequences.fasta -o output.json -he -f "(ab)/(cde)/(fghi)/(jklm)"`

### Module Usage
Hunana can also be imported and used within your Python projects as below:
```
from hunana import Hunana
Hunana('/path/to/sequence.fasta').run()
```

#### Module Parameters
```
The Hunana algorithm returns a list of Position objects each corresponding to a kmer position.

:param seqs: A file handle, a FASTA sequence wrapped in a handle, or a filepath.
:param kmer_len: The length of the kmers to generate (default:  9).
:param header_decode: Whether to use FASTA headers to derive kmer information (default: False).
:param json_result: Whether the results should be returned in json format (default: False).
:param max_samples: The maximum number of samples to use when calculating entropy (default: 10000).
:param iterations: The maximum number of iterations to use when calculating entropy (default: 10).
:param header_format: The format of the header (ex: (id)|(species)|(country))

:type seqs: Union[str, TextIOWrapper, StringIO]
:type kmer_len: str
:type header_decode: bool
:type max_samples: int
:type iterations: int
:type json_result: bool
:type header_format: str
```
