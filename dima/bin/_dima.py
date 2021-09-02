import argparse
import sys

from io import StringIO

from dima import Dima


def get_version():
    if sys.version_info >= (3, 8):
        from importlib.metadata import version
        return version('dima-cli')
    else:
        import pkg_resources
        return pkg_resources.get_distribution('dima-cli').version


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Absolute path to the aligned sequences file in FASTA format.',
                        required=False)
    parser.add_argument('-o', '--output', help='Absolute path to the output file.', required=False, default=None)
    parser.add_argument('-l', '--length', help='The k-mer length (default: 9).', type=int, default=9,
                        choices=range(1, 20), required=False)
    parser.add_argument('-f', '--format',
                        help="The format of the header. Ex: accession|strain|year.", type=str, required=False,
                        default=None)
    parser.add_argument('-s', '--support', help='The minimum threshold for support. (default: 30)', type=int,
                        required=False, default=30)
    parser.add_argument('-p', '--protein', help='The name of the protein being processed. (default: Unknown Protein',
                        type=str, required=False, default='Unknown Protein')
    parser.add_argument('-v', '--version', help='Print the currently installed version of dima-cli.', action='version',
                        version='%(prog)s ' + get_version())
    parser.add_argument('-n', '--fillna', help='Silently fix missing values in the FASTA header with given value.',
                        default=None)

    arguments = parser.parse_args()
    inputx = arguments.input

    if not inputx:
        if sys.stdin.isatty():
            parser.error('Error: The input path is not provided.')
            sys.exit(2)

        # TODO: Here the pipe could just be empty. Need to have a check for that.
        inputx = StringIO(sys.stdin.read())

    try:
        Dima(
            sequences=inputx,
            kmer_length=arguments.length,
            header_format=arguments.format,
            json=True,
            protein_name=arguments.protein,
            support_threshold=arguments.support,
            json_save_path=arguments.output,
            header_fillna=arguments.fillna
        ).run()
    except Exception as ex:
        parser.error(f'Exception while calculating kmers for sequences file {arguments.input}\n{ex}')
        sys.exit(5)

    if arguments.output:
        print(f'Results successfully saved at {arguments.output}')

    sys.exit(0)


if __name__ == '__main__':
    main()
