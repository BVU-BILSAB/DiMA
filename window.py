from collections import Counter
from itertools import islice
from typing import Generator

from datatypes import Position, Variant, VariantDict


class SlidingWindow(object):
    """
        Sliding Window Class

        Gets a zip object containing k-mers from from all the sequences provided classified by position.

        Example:
            >>> from window import SlidingWindow
            >>> window = SlidingWindow(iter[SeqRecord], 9)
            >>> kmers = window.kmers()
            >>> kmer1 = list(kmers[0]) # First k-mer of all sequences
            >>> kmer2 = list(kmers[1]) # Second k-mer of all sequences
    """

    DISALLOWED_CHARS = {'-', 'X', 'B', 'J', 'Z', 'O', 'U'}

    def __init__(self, seqs, kmer_len=9):
        """
            Args:
                seqs: An iterable of type SeqRecord.
                kmer_len: The length of the sliding window (Default: 9).
        """

        self.seqs = seqs
        self.kmer_len = kmer_len

    def _create_variant_dict(self, kmers) -> Generator:
        for kmer in kmers:
            unique = VariantDict(list)
            # Here there's no need to enumerate, you can just append any value because you are essentialy
            # only using len to get the number of elements. There has to be a more elegant way to achive the same effect
            for a, b in enumerate(kmer):
                unique[b].append(a)

            unique.pop('illegal-char', None)

            yield unique

    def _kmers(self) -> zip:
        """
            Extracts k-mers from all the sequences provided.

            Returns:
                Zip: A Zip object containing all k-mers.
        """

        kmers_seqs = (self._window(seq, self.kmer_len) for seq in self.seqs)

        return zip(*kmers_seqs)

    def _window(self, seq, kmer_len: int) -> Generator:
        """
            The actual logic of sliding window.

            Returns:
                A Generator object for all kmers within the alignment
        """

        it = iter(seq)
        result = tuple(islice(it, kmer_len))

        if len(result) == kmer_len:
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

    def _create_position_objects(self, counters) -> Generator:
        """
            Create kmer position objects with entropy, position and variant properties

            Returns:
                A Generator object for Position objects for each kmer position
        """

        for idx, counter in enumerate(counters, start=1):
            yield Position(
                position=idx,
                sequences=self._create_variant_objects(idx, counter)
            )

    def _create_variant_objects(self, idx, variant_counter: Counter) -> Generator:
        variant_objects = (
            Variant(idx, seq, count)
            for seq, count
            in variant_counter.items()
        )

        return variant_objects

    def run(self):
        kmers = self._kmers()
        variant_dicts = self._create_variant_dict(kmers)
        variant_counters = (x.get_counter() for x in variant_dicts)
        kmer_position_objects = self._create_position_objects(variant_counters)
        return kmer_position_objects
