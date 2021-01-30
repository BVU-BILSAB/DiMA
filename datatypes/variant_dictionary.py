from collections import Counter, defaultdict


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
