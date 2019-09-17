"""Script that generates forward and reverse primers from input sequence

TODO:
- argparse
- flag for primer length
- handle files?
- compute primer melting temp?
"""

import re
import sys

seq = str(sys.argv[1])

# check that seq is coposed of ACTG
if bool(re.match('^[acgtAGCT]+$', seq)) != True:
        print("ERROR: input sequence contains invalid characters")
        exit()

# functions
def rev_comp(x):
    """Returns the reverse complement of the input codon"""
    trans_dict = {'a':'t', 't':'a', 'g':'c', 'c':'g'}
    return "".join([i.replace(i, trans_dict[i.lower()]) for i in x])[::-1]

def primer(x):
    return x[:15].lower()

# print primers
print(f"Forward primer: {primer(seq)}")
print(f"Reverse primer: {primer(rev_comp(seq))}")
