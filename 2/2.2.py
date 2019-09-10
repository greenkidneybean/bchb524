#!/usr/bin/env python3
"""Script to search a sequence for a query and return query index and translation frame

Output:
    Codon position
    Translation frame

Default values:
    query="atg"
    seq="gcatcacgttatgtcgactctgtgtggcgatgtctgctggg"

"""

import argparse
import sys

# parse arguments
parser = argparse.ArgumentParser(
    description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
parser.add_argument(
    "--query", 
    help="the substring to be searched within the sequence",
    type=str,
    default="atg"
    )
parser.add_argument(
    "--seq", 
    help="sequence used for query search",
    type=str,
    default="gcatcacgttatgtcgactctgtgtggcgatgtctgctggg"
    )
args = parser.parse_args()

# get index position of query in sequence
value = args.seq.find(args.query)

# error message of no query found
if value == -1:
    print(f'Error: "{args.query}" not found in sequence')

else:
    # print index of first query
    print(f"Codon position: {value}")

    # print translation frame
    frame = value % 3 + 1
    print(f"Translation frame: {frame}")

