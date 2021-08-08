import argparse
import sys

from io import StringIO

from dima import Dima


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Absolute path to the aligned sequences file in FASTA format.',
                        required=False)
    parser.add_argument('-o', '--output', help='Absolute path to the output file.', required=False)
    parser.add_argument('-l', '--length', help='The k-mer length (default: 9).', type=int, default=9,
                        choices=range(1, 20),
                        required=False)
    parser.add_argument('-f', '--format',
                        help="The format of the header. Ex: accession|strain|year.", type=str, required=False,
                        default=None)
    parser.add_argument('-s', '--support', help='The minimum threshold for support. (default: 30)', type=int,
                        required=False, default=30)
    parser.add_argument('-p', '--protein', help='The name of the protein being processed. (default: Unknown Protein',
                        type=str, required=False, default='Unknown Protein')

    arguments = parser.parse_args()
    inputx = arguments.input
    sequences_source = 'file'

    if not inputx:
        if sys.stdin.isatty():
            parser.error('Error: The input path is not provided.')
            sys.exit(2)

        # TODO: Here the pipe could just be empty. Need to have a check for that.
        inputx = StringIO(sys.stdin.read())
        sequences_source = 'string'

    try:
        results = Dima(
            sequences=inputx,
            kmer_length=arguments.length,
            header_format=arguments.format,
            json=True,
            sequences_source=sequences_source,
            protein_name=arguments.protein,
            support_threshold=arguments.support
        ).run()
    except Exception as ex:
        parser.error(f'Exception while calculating kmers for sequences file {arguments.input}\n{ex}')
        sys.exit(5)

    if not arguments.output:
        print(results)
        sys.exit(0)

    with open(arguments.output, 'w') as output:
        output.write(results)

    print(f'Results successfully saved at {arguments.output}')
    sys.exit(0)


if __name__ == '__main__':
    main()
