#!/usr/bin/env python3

"""Script to search a sequence for a query and return query index and translation frame

Output:
    Reverse of input in lower case

Default values:
    codon="ATG"

"""
import argparse

# parse arguments
parser = argparse.ArgumentParser(
    description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
parser.add_argument(
    "--codon", 
    help="the codon to be reversed and in lowercase",
    type=str,
    default="ATG"
    )
args = parser.parse_args()

# reverse and lower the input
print(args.codon[::-1].lower())