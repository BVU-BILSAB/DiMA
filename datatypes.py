import itertools
from collections import Counter, defaultdict

"""
    Datatypes Module
    
    Describes multiple datatypes used in the Hunana and ATAT packages
"""


class MotifClasses(object):
    """ Defines the short and long name of Motifs. """

    I = 'Index'
    Ma = 'Major'
    Mi = 'Minor'
    U = 'Unique'


class VariantDict(defaultdict):
    """
        Data structure for storing sequence indexes

        Describes the data structure for storing the indexes of sequences where a specific variant originates from

        Methods:
            get_counter: Returns a Counter object for all the variants of the current position
    """

    def get_counter(self) -> Counter:
        """
            Get a counter object for the current position's variants

            :return: Returns a counter object for variants at current position
        """

        position = Counter()
        for x in self:
            position[x] = len(self[x])
        return position


class PList(list):
    def get_all_variants(self):
        all_variants = (x.sequences for x in self)
        all_variants = itertools.chain(*all_variants)
        return all_variants

    def get_total_support(self):
        total = [y.count for y in itertools.chain(*(x.sequences for x in self))]
        total = sum(total)
        return total


class Position(dict):
    def __init__(self, position, sequences, supports):
        """
            Data structure for kmer positions

            Describes the data structure for kmer positions within the alignment

            :param position: A zero-based index for position number
            :param sequences: A list of type Variant containing variants seen at current position

            :type position: int
            :type sequences: Generator
        """

        self.position = position
        self.sequences = self._motif_classify(sequences)
        self.supports = supports

    def __setattr__(self, key, value):
        # This really makes me sad, find a way around this mess TODO: fix this please, also in Variant
        dict.__setitem__(self, key, value)

    def __getattr__(self, item):
        return dict.__getitem__(self, item)

    @classmethod
    def _motif_classify(cls, variants) -> list:
        """
        Given a list of Variant objects sort by the count of each, and  classify each variant into motif classes

        :param variants: A list of Variant objects
        :type variants: list

        :return: A list containing Variant objects sorted by count and each variant classified into motif classes
        """

        variants = sorted(variants, key=lambda x: x.count, reverse=True)

        for idx, variant in enumerate(variants):
            if idx == 0:
                variants[idx].motif_short = 'I'
                variants[idx].motif_long = MotifClasses.I
            elif idx == 1:
                variants[idx].motif_short = 'Ma'
                variants[idx].motif_long = MotifClasses.Ma
            elif variants[idx].count > 1:
                variants[idx].motif_short = 'Mi'
                variants[idx].motif_long = MotifClasses.Mi
            else:
                variants[idx].motif_short = 'U'
                variants[idx].motif_long = MotifClasses.U

        return variants


class Variant(dict):
    def __init__(self, position, sequence, count, motif_short=None, motif_long=None):
        """
            Data Structure for kmer variants

            Describes the data structure for kmer variants

            :param position: The position kmer position within the sequence
            :param sequence: The sequence of the given variant
            :param count: The number of times the variant is seen in the alignment at this position

            :type position: int
            :type sequence: str
            :type count: int
        """

        self.position = position
        self.sequence = sequence
        self.count = count
        self.motif_short = motif_short
        self.motif_long = motif_long

    def __setattr__(self, key, value):
        # This really makes me sad, find a way around this mess TODO: fix this please
        dict.__setitem__(self, key, value)

    def __getattr__(self, item):
        return dict.__getitem__(self, item)


class VariantCounter(object):
    def __init__(self):
        self.counters = {}

    def observe(self, s):
        try:
            self.counters[s] += 1
        except KeyError:
            self.counters[s] = 1

    def results(self, matric):
        if matric == 'values':
            return self.counters.values()
        elif matric == 'keys':
            return self.counters.keys()
        else:
            return self.counters
