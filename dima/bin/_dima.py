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
    parser.add_argument('-o', '--output', help='Absolute path to the output file.', required=True)
    parser.add_argument('-t', '--type', help='Output file type.', required=False, default='json',
                        choices=['json', 'xlsx'])
    parser.add_argument('-l', '--length', help='The k-mer length (default: 9).', type=int, default=9, required=False)
    parser.add_argument('-f', '--format',
                        help="The format of the header. Ex: accession|strain|year.", type=str, required=False,
                        default=None)
    parser.add_argument('-s', '--sthresh', help='The minimum threshold for support. (default: 30)', type=int,
                        required=False, default=30)
    parser.add_argument('-q', '--query', help='The name of the sample being processed. (default: Unknown Query',
                        type=str, required=False, default='Unknown Query')
    parser.add_argument('-v', '--version', help='Print the currently installed version of dima-cli.', action='version',
                        version='%(prog)s ' + get_version())
    parser.add_argument('-n', '--fillna', help='Silently fix missing values in the FASTA header with given value.',
                        default=None)
    parser.add_argument('-a', '--alphabet', help='The type of the input sequences (ie: protein/nucleotide, default: '
                                                 'protein))', default="protein", choices=['protein', 'nucleotide'])
    parser.add_argument('-c', '--hcsout', help='Path to save Highly Conserved Sequences (HCS) in JSON format.',
                        required=False)
    parser.add_argument('-e', '--htresh', help='Minimum incidence (percentage) threshold for HCS concatenation.',
                        default=100.0, type=int, required=False)

    arguments = parser.parse_args()
    inputx = arguments.input

    if not inputx:
        if sys.stdin.isatty():
            parser.error('Error: The input path is not provided.')
            sys.exit(2)

        # TODO: Here the pipe could just be empty. Need to have a check for that.
        inputx = StringIO(sys.stdin.read())

    try:
        result_objs = Dima(
            sequences=inputx,
            kmer_length=arguments.length,
            header_format=arguments.format,
            query_name=arguments.query,
            support_threshold=arguments.sthresh,
            header_fillna=arguments.fillna,
            alphabet=arguments.alphabet
        ).run()

        if arguments.type == 'json':
            result_objs.to_json(arguments.output)
        else:
            result_objs.to_excel(arguments.output)

        if arguments.hcsout:
            result_objs.get_hcs(arguments.hcsout, arguments.htresh)

    except Exception as ex:
        parser.error(f'Exception while generating kmers for sequences file {arguments.input}\n{ex}')
        sys.exit(5)

    print(f'Results successfully saved at {arguments.output}')
    sys.exit(0)


if __name__ == '__main__':
    main()
