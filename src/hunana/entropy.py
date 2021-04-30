import math
import random
from typing import Optional, List

from .datatypes import VariantCounter, Position
from scipy.stats import stats


class NormalizedEntropy(object):
    def __init__(self, positions: List[Position], max_samples: Optional[int] = 10000, iterations: Optional[int] = 10):
        """
            Uses the Shannon's Entropy formula to calculate the entropy (amount of disorder) for each k-mer position.

            :param positions: A list of k-mer positions.
            :param max_samples: The maximum number of samples (default: 10000)
            :param iterations: The maximum number of iterations (default: 10)

            :type positions: list[Position]
            :type max_samples: Optional[int]
            :type iterations: Optional[int]
        """

        self.max_samples = max_samples
        self.iterations = iterations
        self.positions = positions

    def run(self):
        for position in self.positions:
            if not position.supports > 0:
                continue

            normalized_entropy = self._calc_normalized_entropy(position.variants_flattened)
            position.entropy = normalized_entropy

            yield position

    def _calc_normalized_entropy(self, flattened_variants):
        flattened_variants = list(flattened_variants)
        random.shuffle(flattened_variants)

        iteration_data = []

        for iteration in range(self.iterations):
            sample_count = random.randint(1, self.max_samples)
            total_iteration_entropy = 0
            samples = VariantCounter()

            for sample in range(sample_count):
                random_variant = random.choice(flattened_variants)
                samples.observe(random_variant)

            for sample_value in samples.results('values'):
                variant_entropy = self._entropy_calculation(sample_value, sample_count)
                total_iteration_entropy += variant_entropy

            iteration_data.append((total_iteration_entropy * -1, 1.0 / float(sample_count)))

        slope, intercept, r_value, p_value, std_err = stats.linregress([y for x, y in iteration_data],
                                                                       [x for x, y in iteration_data])

        return float(intercept)

    @classmethod
    def _entropy_calculation(cls, sample_value, sample_count):
        entropy = (float(sample_value) / float(sample_count)) * \
                  (math.log2(float(sample_value) / float(sample_count)))
        return entropy
