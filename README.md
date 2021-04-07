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
| Argument         	| Type    	| Default 	| Example                                                                                                   	| Description                                                                       	|
|------------------	|---------	|---------	|-----------------------------------------------------------------------------------------------------------	|-----------------------------------------------------------------------------------	|
| -h               	| N/A     	| N/A     	| `hunana -h`                                                                                               	| Prints a summary of all available command-line arguments.                         	|
| -i               	| String  	| N/A     	| `hunana -i '/path/to/alignment.fasta'`                                                                    	| Absolute path to the aligned sequences file in FASTA format.                      	|
| -o               	| String  	| N/A     	| `hunana -i '/path/to/alignment.fasta' -o output.json`                                                     	| Absolute path to the output JSON file.                                            	|
| -l               	| Integer 	| 9       	| `hunana -i '/path/to/alignment.fasta' -l 12`                                                              	| The length of the generated k-mers.                                               	|
| -s               	| Integer 	| 10000   	| `hunana -i '/path/to/alignment.fasta' -s 20000`                                                           	| Maximum number of samples use when calculating entropy.                           	|
| -it              	| Integer 	| 10      	| `hunana -i '/path/to/alignment.fasta' -it 100`                                                            	| Maximum number of iterations used when calculating entropy.                       	|
| -he              	| Boolean 	| False   	| `hunana -i '/path/to/alignment.fasta' -he -f '(type)\|(accession)\|(strain)\|(country)'`                  	| Enables decoding of the FASTA headers to derive details for each generated k-mer. 	|
| -f               	| String  	| N/A     	| `hunana -i '/path/to/alignment.fasta' -he -f '(type)\|(accession)\|(strain)\|(country)'`                  	| The format of the FASTA header in the FASTA Multiple Sequence Alignment.          	|
| -no_header_error 	| Boolean 	| False   	| `hunana -i '/path/to/alignment.fasta' -he -f '(type)\|(accession)\|(strain)\|(country)' -no_header_error` 	| Whether to raise an error if empty items are found in any of the FASTA headers.   	|

#### More Examples
`hunana -i sequences.fasta -o output.json -he -f "(ncbid)/(strain)/(host)/(country)"`

`hunana -i sequences.fasta -o output.json -he -f "(ncbid)/(strain)/(host)|(country)"`

`hunana -i sequences.fasta -o output.json -he -f "(ab)/(cde)/(fghi)/(jklm)"`

`hunana -i sequences.fasta -o output.json -he -f "(ab)/(cde)/(fghi)/(jklm) -no_header_error"`

### Module Usage
Hunana can also be imported and used within your Python projects as below:
```
from hunana import Hunana
Hunana('/path/to/sequence.fasta').run()
```

#### Module Parameters
|    Argument   |             Type             | Default |                             Description                             |
|:-------------:|:----------------------------:|:-------:|:-------------------------------------------------------------------:|
| seqs          | str, TextIOWrapper, StringIO | N/A     | A file handle, a FASTA sequence wrapped in a handle, or a filepath. |
| kmer_len      | int                          | 9       | The length of the kmers to generate.                                |
| header_decode | bool                         | False   | Whether to use FASTA headers to derive kmer information.            |
| header_format | str                          | N/A     | The format of the header (ex: (id)\|(species)\|(country)).          |
| json_result   | bool                         | False   | Whether the results should be returned in json format.              |
| max_samples   | int                          | 1000    | The maximum number of samples to use when calculating entropy.      |
| iterations    | int                          | 10      | The maximum number of iterations to use when calculating entropy.   |