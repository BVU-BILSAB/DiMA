class InvalidSequenceSource(Exception):
    def __init__(self, source: str):
        super(InvalidSequenceSource, self).__init__(f'The sequence source {source} is invalid.'
                                                    f'\nNeeds to be one of:\n\t- file\n\n- string')
