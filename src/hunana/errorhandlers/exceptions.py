class SequenceFileNotFound(Exception):
    def __init__(self, seq_path: str):
        """
            Error raised when the FASTA file path is invalid, or the file is not found.
            
            :param seq_path: The path to the FASTA file.
            :type seq_path: str 
        """

        msg = f'\nThe FASTA file was not found at the following location:\n\t{seq_path}\nAdvice: \n\tPlease check ' \
              f'whether the path is valid, or contains any errors.'

        super(SequenceFileNotFound, self).__init__(msg)


class HeaderDecodeError(Exception):
    def __init__(self, header_format: str):
        """
            Error raised when the correct regex pattern could not be generated.

            :param header_format: The format of the FASTA header.
            :type header_format: str
        """

        msg = f'\nFailed to generate correct regex expression using the header format:\n\t{header_format}\nAdvice:\n\t' \
              f'Make sure the header format you provided accurately reflects the format of all the FASTA headers in ' \
              f'your FASTA file.'

        super(HeaderDecodeError, self).__init__(msg)
