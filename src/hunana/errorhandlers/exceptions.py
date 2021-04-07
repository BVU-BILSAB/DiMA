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


class NoHeaderFormat(Exception):
    def __init__(self):
        """
            Error raised when header decoding is enabled, but no header format is provided.
        """

        msg = 'No header format provided. Please provide the header format.\n\tUsing command-line: Use the flag ' \
              '"hunana -f", or run "hunana -h" for help.\n\tUsing module: Set the "header_format" attribute.'

        super(NoHeaderFormat, self).__init__(msg)


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


class SequenceLengthError(Exception):
    def __init__(self, groups_dict: dict):
        """
            Error raised when not all sequences in the slignment are of equal length.

            :param groups_dict: A dictionary containing sequences grouped by sequence length.
            :type groups_dict: dict
        """

        msg = '\nThe FASTA sequences provided does not appear to be aligned and are of various lengths.\n'

        error_data = []

        for length, sequences in groups_dict.items():
            headers = [sequence.description for sequence in sequences]
            headers_string = '\n\t'.join(headers)

            error_data.append(
                '\nLength: {length}\n\t{seqs}'.format(length=length, seqs=headers_string)
            )

        # Yes, this kind of string concatenation is bad, but it's a single time thing and doesn't cost much
        super(SequenceLengthError, self).__init__(msg + '\n'.join(error_data))


class NoSequencesProvided(Exception):
    def __init__(self):
        """
            Error raised when no sequences are provided by the user.
        """

        msg = 'No sequences are provided. Please make sure your FASTA file is not empty, or invalid.'

        super(NoSequencesProvided, self).__init__(msg)


class InvalidKmerLength(Exception):
    def __init__(self, seq_len: int, kmer_len: int):
        """
            Error raised when the kmer length is bigger than, or equal to the sequence length.

            :param seq_len: The length of the sequences provided by the user.
            :param kmer_len: The length of the kmers that user wants to generate.

            :type seq_len: int
            :type kmer_len: int
        """

        msg = f'The kmer length is bigger than, or equal to the length of the sequenced provided.\n\tKMER LENGTH: ' \
              f'{kmer_len}\n\tSEQUENCE LENGTH: {seq_len}'

        super(InvalidKmerLength, self).__init__(msg)


class HeaderItemCountInvalid(Exception):
    def __init__(self, header: str, desired_count: int, actual_count: int):
        """
            Error raised when the number of items provided in the header format does not match the number of items in
            the actual FASTA header of a sequence.

            :param header: The affected FASTA header.
            :param desired_count: The desired number of header items derived from the header format provided by user.
            :param actual_count: The actual number of header items in the FASTA header.

            :type header: str
            :type desired_count: int
            :type actual_count: int
        """

        msg = f'The header data count does not match.\n\tDESIRED HEADER DATA COUNT: {desired_count}\n\tACTUAL COUNT: ' \
              f'{actual_count}\n\tAFFECTED HEADER: {header}'

        super(HeaderItemCountInvalid, self).__init__(msg)


class HeaderItemEmpty(Exception):
    def __init__(self, header: str):
        """
            Error raised when header data errors are not suppressed (via no_header_data_error) and a header item
            is empty.

            :param header: The affected FASTA header.
            :type header: str
        """

        msg = f'Empty header items found:\n\tAFFECTED HEADER: {header}\n\nYou may set the flag ' \
              f'"no_header_data_error=True" to ignore this error and Hunana shall append "Unknown" to all empty ' \
              f'header items.'

        super(HeaderItemEmpty, self).__init__(msg)
