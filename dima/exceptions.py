class InvalidSequenceSource(Exception):
    def __init__(self):
        super(InvalidSequenceSource, self).__init__(f'\nThe sequence source is invalid.\n'
                                                    f'Needs to be of type StringIO, or str')
