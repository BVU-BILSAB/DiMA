import os
from collections import Counter
from io import TextIOWrapper, StringIO
from itertools import islice, groupby
from typing import List, Union, Iterable

import jsonpickle
from Bio.SeqIO import parse, SeqRecord

from .core import HeaderDecode
from .entropy import NormalizedEntropy
from .datatypes import Position, Variant, VariantDict
from .dynamic_constants import DynamicConstants
from .errorhandlers import SequenceFileNotFound, HeaderDecodeError
from .errorhandlers.exceptions import SequenceLengthError, NoSequencesProvided, InvalidKmerLength, NoHeaderFormat, \
    HeaderItemCountInvalid, HeaderItemEmpty


class Hunana(object):
    DISALLOWED_CHARS = {'-', 'X', 'B', 'J', 'Z', 'O', 'U'}

    def __init__(self, seqs: Union[str, TextIOWrapper, StringIO], kmer_len: int = 9, header_decode: bool = False,
                 json_result: bool = False, max_samples: int = 10000, iterations: int = 10, header_format: str = None,
                 no_header_data_error=False, **kwargs):
        """
            The Hunana algorithm returns a list of Position objects each corresponding to a kmer position.

            :param seqs: A file handle, a FASTA sequence wrapped in a handle, or a filepath.
            :param kmer_len: The length of the kmers to generate (default:  9).
            :param header_decode: Whether to use FASTA headers to derive kmer information (default: False).
            :param json_result: Whether the results should be returned in json format (default: False).
            :param max_samples: The maximum number of samples to use when calculating entropy (default: 10000).
            :param iterations: The maximum number of iterations to use when calculating entropy (default: 10).
            :param header_format: The format of the header (ex: (id)|(species)|(country))
            :param no_header_data_error: Whether missing data in the header during header decode throws an error
            (default: False)

            :type seqs: Union[str, TextIOWrapper, StringIO]
            :type kmer_len: str
            :type header_decode: bool
            :type max_samples: int
            :type iterations: int
            :type json_result: bool
            :type header_format: str
            :type no_header_data_error: bool
        """

        self.seqs = self._get_seqs(seqs)
        self.kmer_len = kmer_len
        self.header_decode = header_decode
        self.json_result = json_result
        self.max_samples = max_samples
        self.iterations = iterations
        self.header_format = header_format
        self.no_header_data_error = no_header_data_error

        self.__dict__.update(kwargs)

        # Let's make sure the sequences are aligned and kmer length is valid
        self._check_seqs()

        # If the user needs header data decoded, we prepare the necessary data here
        if header_decode:
            self._prepare_header_decode()

    def _check_seqs(self):
        """
            This method makes sure that all sequences are of equal length (ie: aligned). If not, it throws an error.
            It also ensures that the k-mer length provided by the user is valid given the length of the sequences.
        """

        if not self.seqs:
            raise NoSequencesProvided()

        groups = groupby(self.seqs, lambda seq: len(seq.seq))
        groups_dict = {length: list(group_seqs) for length, group_seqs in groups}

        if len(groups_dict) != 1:
            raise SequenceLengthError(groups_dict)

        seq_length = list(groups_dict.keys())[0]

        if self.kmer_len >= seq_length:
            raise InvalidKmerLength(seq_length, self.kmer_len)

    def _prepare_header_decode(self):
        if not self.header_format:
            raise NoHeaderFormat()

        desired_header_item_count = len(self.header_format.split('|'))

        for seq in self.seqs:
            header_items = seq.description.split('|')
            actual_header_item_count = len(header_items)

            if actual_header_item_count != desired_header_item_count:
                raise HeaderItemCountInvalid(seq.description, desired_header_item_count, actual_header_item_count)

            if any('' == header_item or header_item.isspace() for header_item in header_items):
                if not self.no_header_data_error:
                    raise HeaderItemEmpty(seq.description)

                header_items = ['Unknown' if item == '' or item.isspace() else item for item in header_items]
                seq.description = '|'.join(header_items)

        DynamicConstants.SEQ_DESCRIPTIONS = [x.description for x in self.seqs]

        if not HeaderDecode.set_header_regex(self.header_format):
            raise HeaderDecodeError(self.header_format)

    @classmethod
    def _create_variant_dict(cls, kmers: zip) -> List[VariantDict]:
        """
            Returns a list of VariantDict (a dictionary of lists).
            TODO: Been a while, forgot what this does, try to understand again later.

            :param kmers: A zip object containing kmers
            :type kmers: zip

            :return: A list of VariantDict.
        """

        positions = []

        for kmer in kmers:
            unique = VariantDict(list)
            # Here there's no need to enumerate, you can just append any value because you are essentialy
            # only using len to get the number of elements. There has to be a more elegant way to achive the same effect
            for a, b in enumerate(kmer):
                unique[b].append(a)
            unique.pop('illegal-char', None)

            positions.append(unique)
        return positions

    @classmethod
    def _get_seqs(cls, seqs: Union[str, TextIOWrapper, StringIO]) -> List[SeqRecord]:
        """
            Checks if the FASTA filepath is valid and file is present, if so, returns a list of SeqRecords for each
            sequence.

            :param seqs: Handle to the file, or the filename as a string.
            :type seqs: Union[str, TextIOWrapper, StringIO]

            :return: A list of SeqRecords for each sequence in the FASTA file.
        """

        if isinstance(seqs, str) and not os.path.isfile(seqs):
            raise SequenceFileNotFound(seqs)

        return list(parse(seqs, 'fasta'))

    def _kmers(self) -> zip:
        """
            Matches each kmer position of all sequences together (ex: all first kmer positions grouped together.)

            :returns: A Zip object containing all k-mers.
        """

        kmers_seqs = (self._window(seq.seq) for seq in self.seqs)
        return zip(*kmers_seqs)

    def _window(self, seq: str) -> Iterable:
        """
            Generates kmers of each sequence in it's respective element (ex: all kmers of sequence 1 in the first
            element of the generator).

            :param seq: The sequence to generate kmers out of.
            :type seq: str

            return: A Generator object containing kmers
        """

        it = iter(seq)
        result = tuple(islice(it, self.kmer_len))

        if len(result) == self.kmer_len:
            if all(ele not in result for ele in self.DISALLOWED_CHARS):
                yield ''.join(result)
            else:
                yield 'illegal-char'

        for elem in it:
            result = result[1:] + (elem,)
            if all(ele not in result for ele in self.DISALLOWED_CHARS):
                yield ''.join(result)
            else:
                yield 'illegal-char'

    def _create_position_objects(self, counters: Iterable[Counter],
                                 variant_dicts: List[VariantDict]) -> Iterable:
        """
            Create kmer position objects with entropy, position and variant properties

            :return A Generator object for Position objects for each kmer position
        """

        for idx, counter in enumerate(counters, start=1):
            yield Position(
                position=idx,
                variants=self._create_variant_objects(idx, counter),
                variants_flattened=list(counter.elements()),
                variant_dict=variant_dicts[idx - 1],
                variant_data=self.header_decode
            )

    def _create_variant_objects(self, idx: int, variant_counter: Counter) -> Iterable[Variant]:
        """
            Creates variant objects to be inserted to Position objects later.

            :param idx: The position number.
            :param variant_counter: The counter containing the variants.

            :type idx: int
            :type variant_counter: Counter

            :return: A Generator of Variant objects.
        """

        num_variants = sum(variant_counter.values())

        variant_objects = (
            Variant(idx, seq, count, self._calc_incidence(count, num_variants))
            for seq, count
            in variant_counter.items()
        )
        return variant_objects

    @classmethod
    def _calc_incidence(cls, variant_hits: int, total_hits: int) -> float:
        """
            Calculates the incidence for a given variant.

            :param variant_hits: The number of times the variant was seen in the sequences at this particular position.
            :param total_hits: The total number of variants.

            :type variant_hits: int
            :type total_hits: int

            :return: The incidence of this particular variant.
        """

        incidence = (float(variant_hits) * 100) / float(total_hits)
        return float(incidence)

    def run(self) -> Union[str, List[Position]]:
        """
            Run the pipeline.

            :return: Returns either json results or a list of Position objects.
        """

        kmers = self._kmers()
        variant_dicts = self._create_variant_dict(kmers)
        variant_counters = (x.get_counter() for x in variant_dicts)
        kmer_position_objects = self._create_position_objects(variant_counters, variant_dicts)
        entropy = NormalizedEntropy(self.max_samples, self.iterations, list(kmer_position_objects)).run()
        results = list(entropy)

        if self.json_result:
            return jsonpickle.encode(results, indent=2, unpicklable=False)
        else:
            return results
