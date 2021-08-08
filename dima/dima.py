import tempfile
from typing import Union, Optional, Literal, overload
from .helpers import get_results_json, Results, get_results_objs

from dima.exceptions import InvalidSequenceSource


class Dima(object):
    @overload
    def __init__(
            self,
            sequences: str,
            sequences_source: str,
            kmer_length: Optional[int] = 9,
            json: Optional[bool] = False,
            header_format: Optional[str] = None,
            support_threshold: Optional[int] = 30,
            protein_name: Optional[str] = 'Unknown Protein'
    ):
        pass

    def __init__(
            self,
            sequences: str,
            sequences_source: Literal['string', 'file'],
            kmer_length: Optional[int] = 9,
            json: Optional[bool] = False,
            header_format: Optional[str] = None,
            support_threshold: Optional[int] = 30,
            protein_name: Optional[str] = 'Unknown Protein'
    ):
        """
            The DiMA algorithm returns a list of Position objects each corresponding to a kmer position.

            :param sequences: A file path, or a string containing the aligned FASTA sequences.
            :param kmer_length: The length of the kmers to generate (default:  9).
            :param json: Whether the results should be returned in json format (default: False).
            :param header_format: The format of the header (ex: (id)|(species)|(country)) (default: False).
            :param sequences_source: The source used for the sequences (ie: whether file, or string)
            :param support_threshold: The support threshold below which k-mer positions will be considered
                to have low support.
            :param protein_name: The name of the protein we are dealing with.

            :type sequences: str
            :type kmer_length: Optional[int]
            :type json: Optional[bool]
            :type header_format: Optional[str]
            :type sequences_source: Literal['string', 'file']
            :type support_threshold: Optional[int]
            :type protein_name: str
        """

        if sequences_source != 'string' and sequences_source != 'file':
            raise InvalidSequenceSource(sequences_source)

        self.sequence_file = self._save_sequences_file(sequences) if sequences_source == 'string' else sequences
        self.kmer_length = kmer_length
        self.json = json
        self.header_format = header_format
        self.support_threshold = support_threshold
        self.protein_name = protein_name

    @classmethod
    def _save_sequences_file(cls, sequences: str) -> str:
        """
            Saves the raw aligned FASTA sequences to a temporary file, and returns the full path.

            :param sequences: A bunch of aligned FASTA sequences.
            :type sequences: str

            :return: The full path to the temporary file populated with the FASTA sequences.
        """

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write(sequences)

        return f.name

    def run(self) -> Union[str, Results]:
        arguments = {
            'path': self.sequence_file,
            'kmer_length': self.kmer_length,
            'header_format': self.header_format.split('|') if self.header_format else None,
            'support_threshold': self.support_threshold,
            'protein_name': self.protein_name
        }

        if self.json:
            return get_results_json(**arguments)
        else:
            return get_results_objs(**arguments)
