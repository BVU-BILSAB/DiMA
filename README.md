# Hunana
A modular implementation of Hunana. A sub-module of ViVA.

## Installation

**OPTION 1**

`pip install git+https://github.com/pu-sds/hunana.git`

**OPTION 2**

```
git clone https://github.com/pu-sds/hunana.git
cd hunana
python setup.py install
```

**OPTION 3**

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
    "position": 1,
    "entropy": 0.0,
    "supports": 2,
    "sequences": [
      {
        "position": 1,
        "sequence": "MASPGLHLL",
        "count": 2,
        "conservation": 100.0,
        "motif_short": "I",
        "motif_long": "Index"
      }
    ],
    "variants": 1,
    "kmertypes: [
      'MASPGLHLL'
    ]
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
    "position": 1,
    "entropy": 0.0,
    "supports": 2,
    "sequences": [
      {
        "position": 1,
        "sequence": "MASPGLHLL",
        "count": 2,
        "conservation": 100.0,
        "motif_short": "I",
        "motif_long": "Index",
        "type": [
          "tr",
          "tr"
        ],
        "id": [
          "A0A2Z4MTJ4",
          "A0A0K2GVL2"
        ],
        "strain": [
          "A0A2Z4MTJ4_9HIV2_Envelope_glycoprotein_gp160_OS_Human_immunodeficiency_virus_2_OX_11709_GN_env_PE_4_SV_1",
          "A0A0K2GVL2_9HIV2_Envelope_glycoprotein_gp160_OS_Human_immunodeficiency_virus_2_OX_11709_GN_env_PE_4_SV_1"
        ]
      }
    ],
    "variants": 1,
    "kmertypes: [
      'MASPGLHLL'
    ]
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

    :param seq_path: The absolute path to the MSA file in FASTA format.
    :param kmer_len: The length of the kmers to generate (default:  9).
    :param header_decode: Whether to use FASTA headers to derive kmer information (default: False).
    :param json_result: Whether the results should be returned in json format (default: False).
    :param max_samples: The maximum number of samples to use when calculating entropy (default: 10000).
    :param iterations: The maximum number of iterations to use when calculating entropy (default: 10).
    
    :type seq_path str
    :type kmer_len: str
    :type header_decode: bool
    :type json_result: bool
    :type max_samples: int
    :type iterations: int
```
