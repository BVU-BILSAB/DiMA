# Hunana
A modular implementation of Hunana. A sub-module in the ViVA workflow

## Installing Requirements:
`pip install -r requirements.txt`

## Usage:

### Basic Usage
`python run.py -i sequences.fasta -o output.json -l 9`

`python run.py -i sequences.fasta | grep supports`

#### Example Output
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
    "variants": 1
  }
]
```

### Generate Variant Data
The flag --he/--header along with the -f/--format header can be used to generate data for each variant using the metadata from the fasta sequence header.

`python run.py -i sequences.fasta -o output.json -he -f "(type)|(id)|(strain)"`

#### Example Output
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
    "variants": 1
  }
]
```
Each componant (ex: id, strain, country, etc)of the header needs to be wrapped in brackets. Any separator (Ex: |, /, _, etc) can be used.

#### More Examples
`python run.py -i sequences.fasta -o output.json -he -f "(ncbid)/(strain)/(host)/(country)"`
`python run.py -i sequences.fasta -o output.json -he -f "(ncbid)/(strain)/(host)|(country)"`
`python run.py -i sequences.fasta -o output.json -he -f "(ab)/(cde)/(fghi)/(jklm)"`
