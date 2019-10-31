"""Script to identify if primer input is a reverse complement palindrome

Input:
    argument 1 (str): primer sequence

TODO:
- pipe 6.1.py into 6.2.py to check for reverse complement palindromes in primers
"""

import re
import sys

seq = str(sys.argv[1])

# check that seq is composed of ACTG characters
if bool(re.match('^[acgtAGCT]+$', seq)) != True:
    print("ERROR: input sequence contains invalid characters")
    exit()

# functions
def rev_comp(x):
    """Returns the reverse complement of the input codon"""
    trans_dict = {'a':'t', 't':'a', 'g':'c', 'c':'g'}
    return "".join([i.replace(i, trans_dict[i.lower()]) for i in x])[::-1]

def rev_palindrome(x):
    """checks if input sequence is a reverse palindrome"""
    y = len(x) // 2
    return x[:y].lower() == rev_comp(x)[:y]

print(rev_palindrome(seq))
