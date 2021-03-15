import itertools
import re
from collections import defaultdict
from typing import Generator, Iterable

from .motif_classes import MotifClasses
from ..dynamic_constants import DynamicConstants


class Position(dict):
    def __init__(self, position: int, variants: Iterable, variants_flattened: list, variant_dict: defaultdict,
                 entropy: float = None, variant_data: bool = False):
        """
            Data structure for kmer positions

            Describes the data structure for kmer positions within the alignment

            :param position: The k-mer position number.
            :param variants: A list of type Variant containing variants seen at current position
            :param variants_flattened: A flattened list of all variants. Note: Only used for processing
            :param variant_dict: A default dictionary of lists to store the sequence idx for later getting description data
            :param entropy: The Shannon entropy at the current kmer position
            :param variant_data: Whether to derive variant data from the sequence headers.

            :type position: int
            :type variants: Generator
            :type variants_flattened: list
            :type variant_dict: defaultdict
            :type entropy: float
            :type variant_data: bool

            The attributes of this class are converted into keys when json_results=True

            Attributes:
                - Position: A zero-based index for kmer position.
                - Entropy: The calculated entropy (Snannon's Entropy) for a particular kmer position.
                - Supports: The number of valid (no gaps, no invalid characters) variants.
                - Variants: A list of variants for a particular kmer position.
                - kmer_types: Distinct variants that are different from the index variant.
        """

        supports = len(variants_flattened)
        variants = self._motif_classify(variants)

        self.position = position
        self.entropy = entropy
        self.variants_flattened = variants_flattened
        self.supports = supports
        self.variants = variants
        self.kmer_types = self._set_kmer_types(supports, variants)

        self._set_desc_data(variant_dict) if variant_data else None

    @classmethod
    def _set_kmer_types(cls, supports: int, variants: list) -> dict:
        """
            Calculates the incidence of distinct variants (excluding Index variant) and generates a list of distinct
            variants (excluding Index variant)

            :param supports: The total number of valid k-mers for a given position .
            :param variants: The list (of type Variant) of distinct k-mers for a given position.

            :type supports: int
            :type variants: list

            :returns: A dictionary containing the incidence of distinct variants and a list of distinct variants.
        """

        # Here we minus 1 because we need to exclude the index
        variant_count = len(variants)

        if variant_count == 0 or supports == 0:
            return {'incidence': 0, 'types': []}

        incidence = ((len(variants) - 1) / supports) * 100
        kmer_types = [variant.sequence for variant in variants if variant.motif_short != 'I']

        return {'incidence': incidence, 'types': kmer_types}

    def _set_desc_data(self, variant_dict):
        """
            Sets the data from the header as attributes in the variant object.

            :param variant_dict: A defaultdict of list containing idx of sequences
            :type variant_dict: defaultdict
        """

        expr = re.compile(DynamicConstants.HEADER_REGEX)

        for dict_variant, variant in itertools.product(variant_dict, self.variants):
            if dict_variant != variant.sequence:
                continue
            idx = variant_dict[dict_variant]

            for ids in idx:
                header = DynamicConstants.SEQ_DESCRIPTIONS[ids]

                mapping = [x.groupdict() for x in expr.finditer(header)][0]

                for key, value in mapping.items():
                    current_value = variant.get(key)

                    if not current_value:
                        variant[key] = [value]
                        continue

                    variant[key] = current_value + [value]

    def __setattr__(self, key, value):
        dict.__setitem__(self, key, value)

    def __getattr__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            raise AttributeError

    def __getstate__(self):
        state = self.copy()

        # Because this is only needed to calculate entropy
        del state['variants_flattened']

        return state

    def __setstate__(self, state):
        self.__dict__.update(state)

    @classmethod
    def _motif_classify(cls, variants: Iterable) -> list:
        """
            Given a list of Variant objects sort by the count of each, and  classify each variant into motif classes

            :param variants: A list of Variant objects
            :type variants: Generator

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
