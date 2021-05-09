# Module Usage
DiMA can also be imported and used within your Python projects as below:
``` python
from dima import Dima
Dima('/path/to/sequence.fasta').run()
```

## Examples
Let us assume we have the following aligned FASTA:
```
>A|CY021716|A/AA/Huston/1945|USA
MERIKELRNLMSQSRTREILTKTTVDHMAIIKKYTSGRQEKNPSLRMKWMMAMKYPITADKRITEMIPER

>A|CY020292|A/AA/Marton/1943|USA
NEQGQTLWSKMNDAGSDRVMVSPLAVTWWNRNGPMTSTVHYPKIYKTYFEKVERLKHGTFGPVHFRNQVK

>A|CY083917|A/Aalborg/INS132/2009|Denmark
MERIKELRDLMSQSRTREILTKTTVDHMAIIKKYTSGRQEKNPALRMKWMMAMRYPITADKRIMDMIPER
```
### Basic Usage
```python
from dima import Dima
from io import StringIO

fasta_sequences = """>A|CY021716|A/AA/Huston/1945|USA
MERIKELRNLMSQSRTREILTKTTVDHMAIIKKYTSGRQEKNPSLRMKWMMAMKYPITADKRITEMIPER
>A|CY020292|A/AA/Marton/1943|USA
NEQGQTLWSKMNDAGSDRVMVSPLAVTWWNRNGPMTSTVHYPKIYKTYFEKVERLKHGTFGPVHFRNQVK
>A|CY083917|A/Aalborg/INS132/2009|Denmark
MERIKELRDLMSQSRTREILTKTTVDHMAIIKKYTSGRQEKNPALRMKWMMAMRYPITADKRIMDMIPER"""

# We create a handle for the text-based FASTA
handle = StringIO(fasta_sequences)

# Then run DiMA with default parameters
results = Dima(handle).run()
```

### Advanced Usage
```python
from dima import Dima
from io import StringIO

fasta_sequences = """>A|CY021716|A/AA/Huston/1945|USA
MERIKELRNLMSQSRTREILTKTTVDHMAIIKKYTSGRQEKNPSLRMKWMMAMKYPITADKRITEMIPER
>A|CY020292|A/AA/Marton/1943|USA
NEQGQTLWSKMNDAGSDRVMVSPLAVTWWNRNGPMTSTVHYPKIYKTYFEKVERLKHGTFGPVHFRNQVK
>A|CY083917|A/Aalborg/INS132/2009|Denmark
MERIKELRDLMSQSRTREILTKTTVDHMAIIKKYTSGRQEKNPALRMKWMMAMRYPITADKRIMDMIPER"""

# We create a handle for the text-based FASTA
handle = StringIO(fasta_sequences)

# Then run DiMA with default parameters
results = Dima(handle, header_decode=True, header_format='(type)|(accession)|(strain)|(country)').run()
```

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

## Module Parameters
|    Argument   |             Type             | Default |                             Description                             |
|:-------------:|:----------------------------:|:-------:|:-------------------------------------------------------------------:|
| seqs          | str, TextIOWrapper, StringIO | N/A     | A file handle, a FASTA sequence wrapped in a handle, or a filepath. |
| kmer_len      | int                          | 9       | The length of the kmers to generate.                                |
| header_decode | bool                         | False   | Whether to use FASTA headers to derive kmer information.            |
| header_format | str                          | N/A     | The format of the header (ex: (id)\|(species)\|(country)).          |
| json_result   | bool                         | False   | Whether the results should be returned in json format.              |
| max_samples   | int                          | 10000    | The maximum number of samples to use when calculating entropy.      |
| iterations    | int                          | 10      | The maximum number of iterations to use when calculating entropy.   |
| no_header_error | bool                       | False   | Whether to raise an error if empty items are found in any of the FASTA headers.   |