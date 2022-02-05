import tempfile
from io import StringIO
from shutil import copyfileobj
from typing import Union, Optional
from .helpers import Results, get_results_objs

from dima.exceptions import InvalidSequenceSource, ExcelFilePathNotProvided, UnknownOutputFileFormat


class Dima(object):
    def __init__(
            self,
            sequences: Union[StringIO, str],
            kmer_length: Optional[int] = 9,
            header_format: Optional[str] = None,
            support_threshold: Optional[int] = 30,
            protein_name: Optional[str] = 'Unknown Protein',
            header_fillna: Optional[str] = None
    ):
        """
            The DiMA algorithm returns a list of Position objects each corresponding to a kmer position.

            :param sequences: A file path, or a string containing the aligned FASTA sequences.
            :param kmer_length: The length of the kmers to generate (default:  9).
            :param header_format: The format of the header (ex: id|species|country) (default: None).
            :param support_threshold: The support threshold below which k-mer positions will be considered
                to have low support.
            :param protein_name: The name of the protein we are dealing with.
            :param header_fillna: If there are empty items in the FASTA header (when header_format != None), replace
            with this value.

            :type sequences: Union[StringIO, str]
            :type kmer_length: Optional[int]
            :type header_format: Optional[str]
            :type support_threshold: Optional[int]
            :type protein_name: str
            :type header_fillna: Optional[str]

            Example 1:

            >>> from dima import Dima
            >>> Dima("path/to/seqs.afa").run()

            Example 2:

            >>> from io import StringIO
            >>> from dima import Dima
            >>> aligned_fasta = '''>A321223|Corona_1|2012\nSRDXFCYVGHUJN\n>A321223|Corona_2|2012\nSRDXFCYVGHUJN'''
            >>> Dima(StringIO(aligned_fasta)).run()
        """

        if not isinstance(sequences, StringIO) and not isinstance(sequences, str):
            raise InvalidSequenceSource()

        self.sequence_file = self._save_sequences_file(sequences) if isinstance(sequences, StringIO) else sequences
        self.kmer_length = kmer_length
        self.header_format = header_format
        self.support_threshold = support_threshold
        self.protein_name = protein_name
        self.header_fillna = header_fillna

    @classmethod
    def _save_sequences_file(cls, sequences: StringIO) -> str:
        """
            Saves the raw aligned FASTA sequences to a temporary file, and returns the full path.

            :param sequences: A bunch of aligned FASTA sequences in a StringIO object.
            :type sequences: StringIO

            :return: The full path to the temporary file populated with the FASTA sequences.
        """

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            sequences.seek(0)
            copyfileobj(sequences, f)

        return f.name

    def run(self) -> Results:
        results_objects = get_results_objs(
            path=self.sequence_file,
            kmer_length=self.kmer_length,
            header_format=self.header_format.split('|') if self.header_format else None,
            support_threshold=self.support_threshold,
            protein_name=self.protein_name,
            header_fillna=self.header_fillna
        )

        return results_objects

    def _handle_save_results(self, results: Results) -> Optional[Union[Results, str]]:
        """
        A simple method that takes care of all the results file handling.

        :param results: The results object generated after DiMA has been run.
        :type results: Results

        :returns: If no path is given to save JSON, then the results can either be printed to STDOUT, or returned as
            a string. This behaviour can be controlled using the **print** boolean value.
        """

        # If no path is given then we can either return objs, or json, OR print json to stdout (this is cli mode)

