class InvalidSequenceSource(Exception):
    def __init__(self):
        super(InvalidSequenceSource, self).__init__(f'\nThe sequence source is invalid.\n'
                                                    f'Needs to be of type StringIO, or str')


class ExcelFilePathNotProvided(Exception):
    def __init__(self):
        super(ExcelFilePathNotProvided, self).__init__('When saving as .xlsx a save path needs to be provided.')


class UnknownOutputFileFormat(Exception):
    def __init__(self, user_given_format: str):
        super(UnknownOutputFileFormat, self).__init__(f'The provided file output format ({user_given_format}) '
                                                     f'is invalid (options: json, xlsx)')
