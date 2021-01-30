import argparse, sys
import json
import sys

from Bio.SeqIO import parse
from hunana import SlidingWindow, NormalizedEntropy
from core import HeaderDecode

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='Absolute path to the aligned sequences file in FASTA format.')
parser.add_argument('-o', '--output', help='Absolute path to the output file.')
parser.add_argument('-l', '--length', help='The k-mer length (default: 9)', type=int, default=9, choices=range(1, 15))
parser.add_argument('-he', '--header', help="Should the header data be used to derive the details for variants?",
                    action='store_true')
parser.add_argument('-f', '--format', help="The format of the header. Ex: (id)|(species)|(country). Each item enclosed "
                                           "in brackets with any character used as separator.", required=False)

arguments = parser.parse_args()

if arguments.header:
    if not arguments.format:
        parser.error("The header format (-f/--format) needs to be provided if header parsing (-he/--header) parsing "
                     "is enabled")
        sys.exit(6)

    if not HeaderDecode().set_header_regex(arguments.format):
        parser.error("Failed to set header parsing options")
        sys.exit(7)

if not arguments.input:
    parser.error('Error: The input path is not provided.')
    sys.exit(2)

try:
    sequences = open(arguments.input, 'r')
except FileNotFoundError as err:
    print(str(err.strerror), file=sys.stderr)
    sys.exit(3)

try:
    parsed_sequences = parse(sequences, 'fasta')
except Exception:
    parser.error(f'Unknown exception while parsing the provided input file {arguments.input}')
    sys.exit(4)

try:
    kmer_positions = SlidingWindow(parsed_sequences, arguments.length,arguments.header).run()
    entropy = NormalizedEntropy(10000, 10, list(kmer_positions)).run()
    sequences.close()
except Exception:
    parser.error(f'Exception while calculating kmers for sequences file {arguments.input}')
    sys.exit(5)

json_results = json.dumps(list(entropy), indent=2)

if not arguments.output:
    print(json_results)
    sys.exit(0)

with open(arguments.output, 'w') as output:
    output.write(json_results)

print(f'Results successfully saved at {arguments.output}')
sys.exit(0)
