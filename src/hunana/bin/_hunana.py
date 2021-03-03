import argparse
import sys

from io import StringIO
from hunana import Hunana


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Absolute path to the aligned sequences file in FASTA format.',
                        required=False)
    parser.add_argument('-o', '--output', help='Absolute path to the output file.', required=False)
    parser.add_argument('-l', '--length', help='The k-mer length (default: 9).', type=int, default=9,
                        choices=range(1, 15),
                        required=False)
    parser.add_argument('-s', '--samples', help='Max number of samples use when calculating entropy (default: 10000).',
                        type=int, default=10000, required=False)
    parser.add_argument('-it', '--iterations',
                        help='Max number of iterations used when calculating entropy (default: 10).',
                        type=int, default=10, required=False)
    parser.add_argument('-he', '--header', help="Should the header data be used to derive the details for variants?.",
                        action='store_true', required=False)
    parser.add_argument('-f', '--format',
                        help="The format of the header. Ex: (id)|(species)|(country). Each item enclosed "
                             "in brackets with any character used as separator.", required=False,
                        default=None)

    arguments = parser.parse_args()

    if arguments.header:
        if not arguments.format:
            parser.error(
                "The header format (-f/--format) needs to be provided if header parsing (-he/--header) parsing "
                "is enabled")
            sys.exit(6)

    inputx = arguments.input

    if not inputx:
        if sys.stdin.isatty():
            parser.error('Error: The input path is not provided.')
            sys.exit(2)

        # TODO: Here the pipe could just be empty. Need to have a check for that.
        inputx = StringIO(sys.stdin.read())

    try:
        results = Hunana(inputx, arguments.length, arguments.header, True, arguments.samples,
                         arguments.iterations, arguments.format).run()
    except Exception:
        parser.error(f'Exception while calculating kmers for sequences file {arguments.input}')
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
