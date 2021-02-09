class Variant(dict):
    def __init__(self, position, sequence, count, conservation, motif_short=None, motif_long=None):
        """
            Data Structure for kmer variants

            Describes the data structure for kmer variants

            :param position: The position kmer position within the sequence
            :param sequence: The sequence of the given variant
            :param count: The number of times the variant is seen in the alignment at this position
            :param conservation: The percentage conservation of this variant for this position
            :param motif_short: The short name motif classification for this variant
            :param motif_long: The long name motif classification for this variant
            :param idx: A list containing the idx of the sequences where this variant was observed
            :param strain: A list containing the strain names of the sequences where this variant was observed
            :param country: A list containing the country names of the sequences where this variant was observed
            :param host: A list containing the host names of the sequences where this variant was observed

            :type position: int
            :type sequence: str
            :type count: int
            :type conservation: float
            :type motif_short: str
            :type motif_long: str
            :type idx: list
            :type strain: list
            :type country: list
            :type host: list
        """

        self.position = position
        self.sequence = sequence
        self.count = count
        self.conservation = conservation
        self.motif_short = motif_short
        self.motif_long = motif_long

    def __setattr__(self, key, value):
        # This really makes me sad, find a way around this mess TODO: fix this please, also in Variant
        dict.__setitem__(self, key, value)

    def __getattr__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            raise AttributeError

    def __getstate__(self):
        state = self.copy()
        state = {key: value for key, value in state.items() if value}

        return state
