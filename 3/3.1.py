#!/usr/bin/env python3
"""3.1 - Script to characterize a gene sequence from input file

Output:
    Does gene start with Met ("ATG") codon: bool
    Does gene have a frame-1 Met codon: bool
    Length of gene: int
    Amino-acid length of gene: int
    GC content (%): float

Defaults:
    seq_file = "anthrax_sasp.nuc"
"""

import argparse

# parse arguments
parser = argparse.ArgumentParser(
    description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument(
    "seq_file", 
    help="sequence file to be parsed",
    type=str,
    default="anthrax_sasp.nuc"
)
args = parser.parse_args()

# check that file exists and that there's something in it

# extract and concatenate seq from file

# generate output