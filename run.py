import argparse, sys
import json

from Bio.SeqIO import parse
from window import SlidingWindow

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='Absolute path to the aligned sequences file in FASTA format.')
parser.add_argument('-o', '--output', help='Absolute path to the output file.')
parser.add_argument('-l', '--length', help='The k-mer length (default: 9)', type=int, default=9, choices=range(1, 15))

arguments = parser.parse_args()

if not arguments.input or not arguments.output:
    print('Error: The input and output path names are not provided.')
    sys.exit(2)

try:
    sequences = open(arguments.input, 'r')
except FileNotFoundError as err:
    print(str(err.strerror))
    sys.exit(3)

try:
    parsed_sequences = parse(sequences, 'fasta')
    sequences.close()
except Exception:
    print(f'Unknown exception while parsing the provided input file {arguments.input}')
    sys.exit(4)

try:
    kmer_positions = SlidingWindow(parsed_sequences, arguments.length).run()
except Exception:
    print(f'Exception while calculating kmers for sequences file {arguments.input}')
    sys.exit(5)

with open(arguments.output, 'w') as output:
    output.write(json.dumps(list(kmer_positions), indent=2))

print(f'Results successfully saved at {arguments.output}')
