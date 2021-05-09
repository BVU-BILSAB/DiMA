# Command-Line Usage
Once installation is complete, an executable will be added to PATH which can be accessed as below:

**Linux**

`dima-cli -h`

**Windows**

`dima-cli.exe -h`

**MacOS**

`dima-cli -h`

## Basic Usage
`dima-cli -i sequences.fasta -o output.json -l 9`

`dima-cli -i sequences.fasta | grep supports`

### Example Output
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

## Advanced Usage
The flag --he/--header along with the -f/--format header can be used to generate data for each variant using the metadata from the fasta sequence header.

`dima-cli -i sequences.fasta -o output.json -he -f "(type)|(id)|(strain)"`

Each componant (ex: id, strain, country, etc)of the header needs to be wrapped in brackets. Any separator (Ex: |, /, _, etc) can be used.

!!! Consideration caution

    How to deal with missing information in the FASTA header?. Glad you asked!.
    Consider the below FASTA file:
    ```
        >A|CY021716|A/AA/Huston/1945|
        MERIKELRNLMSQSRTREILTKTTVDHMAIIKKYTSGRQEKNPSLRMKWMMAMKYPITADKRITEMIPER
        
        >A|CY020292|A/AA/Marton/1943|USA
        NEQGQTLWSKMNDAGSDRVMVSPLAVTWWNRNGPMTSTVHYPKIYKTYFEKVERLKHGTFGPVHFRNQVK
        
        >A|CY083917|A/Aalborg/INS132/2009|Denmark
        MERIKELRDLMSQSRTREILTKTTVDHMAIIKKYTSGRQEKNPALRMKWMMAMRYPITADKRIMDMIPER
    ```
    The first sequence does not contain the Country of Collection. By default, DiMA would raise an exception `
    HeaderItemEmpty`.
    
    To override this behavior, the `no_header_error` parameter can be used to replace missing
    header information with "Unknown".

    **PS:** These kind of sequences with missing information are common when exported from NCBI VIrus.

### Example Output
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

### Command-Line Arguments
| Argument         	| Type    	| Default 	| Example                                                                                                   	| Description                                                                       	|
|------------------	|---------	|---------	|-----------------------------------------------------------------------------------------------------------	|-----------------------------------------------------------------------------------	|
| -h               	| N/A     	| N/A     	| `dima-cli -h`                                                                                               	| Prints a summary of all available command-line arguments.                         	|
| -i               	| String  	| N/A     	| `dima-cli -i "/path/to/alignment.fasta"`                                                                    	| Absolute path to the aligned sequences file in FASTA format.                      	|
| -o               	| String  	| N/A     	| `dima-cli -i "/path/to/alignment.fasta" -o output.json`                                                     	| Absolute path to the output JSON file.                                            	|
| -l               	| Integer 	| 9       	| `dima-cli -i "/path/to/alignment.fasta" -l 12`                                                              	| The length of the generated k-mers.                                               	|
| -s               	| Integer 	| 10000   	| `dima-cli -i "/path/to/alignment.fasta" -s 20000`                                                           	| Maximum number of samples use when calculating entropy.                           	|
| -it              	| Integer 	| 10      	| `dima-cli -i "/path/to/alignment.fasta" -it 100`                                                            	| Maximum number of iterations used when calculating entropy.                       	|
| -he              	| Boolean 	| False   	| `dima-cli -i "/path/to/alignment.fasta" -he -f "(type)\|(accession)\|(strain)\|(country)"`                  	| Enables decoding of the FASTA headers to derive details for each generated k-mer. 	|
| -f               	| String  	| N/A     	| `dima-cli -i "/path/to/alignment.fasta" -he -f "(type)\|(accession)\|(strain)\|(country)"`                  	| The format of the FASTA header in the FASTA Multiple Sequence Alignment.          	|
| -no_header_error 	| Boolean 	| False   	| `dima-cli -i "/path/to/alignment.fasta" -he -f "(type)\|(accession)\|(strain)\|(country)" -no_header_error` 	| Whether to raise an error if empty items are found in any of the FASTA headers.   	|

### More Examples
`dima-cli -i sequences.fasta -o output.json -he -f "(ncbid)/(strain)/(host)/(country)"`

`dima-cli -i sequences.fasta -o output.json -he -f "(ncbid)/(strain)/(host)|(country)"`

`dima-cli -i sequences.fasta -o output.json -he -f "(ab)/(cde)/(fghi)/(jklm)"`

`dima-cli -i sequences.fasta -o output.json -he -f "(ab)/(cde)/(fghi)/(jklm) -no_header_error"`
