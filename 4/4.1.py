#!/usr/bin/env python3
"""4.1 - Return reverse complement codon

Input: codon

Output: reverse complement of condon

Defaults:
    input = "ATG"
"""

import argparse

parser = argparse.ArgumentParser(
    description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument(
    "--codon", 
    help="codon to be reversed and complemented",
    type=str,
    default="ATG"
)
args = parser.parse_args()

def rev_comp(codon):
    """Returns the reverse complement of the input codon"""
    trans_dict = {'a':'t', 't':'a', 'g':'c', 'c':'g'}
    return "".join([i.replace(i, trans_dict[i.lower()]) for i in codon])[::-1]

# check that codon contains only a,c,g,t
if (bool(re.match('^[acgt]+$', codon))) != True:
    print("Error: input is not a valid codon")

# retun reverse complement of input codon
print(rev_comp(args.codon))