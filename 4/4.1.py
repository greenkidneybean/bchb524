#!/usr/bin/env python3
"""4.1 - Return reverse complement codon

Input: codon (str) - string that consist of only A, C, T, and G charcters

Output: reverse complement of condon

Defaults:
    input = "ATG"
"""

import argparse
import re

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

# function to generate reverse codon
# note: stripping-down function from lec 4 slide 9 series if conditional statements and using dictionary
def rev_comp(codon):
    """Returns the reverse complement of the input codon"""
    trans_dict = {'a':'t', 't':'a', 'g':'c', 'c':'g'}
    if len(codon) != 3:
        print(f"ERROR: input codon of length {len(codon)} is not 3")
    return "".join([i.replace(i, trans_dict[i.lower()]) for i in codon])[::-1]

# check that codon contains only a,c,g,t
# note: not yet covered in class but also not a necessary check based on hw description
if bool(re.match('^[acgtAGCT]+$', args.codon)) != True:
    print("ERROR: input is not a valid codon")
    exit()

# retun reverse complement of input codon
print(rev_comp(args.codon))