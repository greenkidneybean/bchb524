"""Script that generates reverse complement of two input primer sequences

Note: handles only two input arguments

Input:
    argument 1 (str): forward primer
    argument 2 (str): reverse primer

Output:
    reverse complement for forward primer
    reverse complement for reverse primer

TODO:
- argparse
- handle files?
- compute primer melting temp?
- identify the invalid characters
- handle file input, designed to take multiline input and split?
"""

import re
import sys

primer_F = str(sys.argv[1])
primer_R = str(sys.argv[2])

primers = [primer_F, primer_R]

# check that primers are composed of nucleotide characters (actg)
for i in primers:
    if bool(re.match('^[acgtAGCT]+$', i)) != True:
        print("ERROR: input primer contains invalid characters")
        exit()

# functions
def rev_comp(x):
    """Returns the reverse complement of the input codon"""
    trans_dict = {'a':'t', 't':'a', 'g':'c', 'c':'g'}
    return "".join([i.replace(i, trans_dict[i.lower()]) for i in x])[::-1]

# print primers
print(rev_comp(primer_F))
print(rev_comp(primer_R))
