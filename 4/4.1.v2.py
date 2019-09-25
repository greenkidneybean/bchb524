#!/usr/bin/env python3
"""4.1 - Return reverse complement codon

Input: codon (str) - string that consist of only A, C, T, and G charcters

Output: reverse complement of condon

Defaults:
    input = "ATG"
"""

# functions

def rev_seq(seq):
    return seq[::-1]

def complement_seq(nuc):
    if nuc == "A":
        comp = "T"
    elif nuc == "T":
        comp = "A"
    elif nuc == "C":
        comp = "G"
    elif nuc == "G":
        comp = "C"
    else:
        comp = nuc
    return comp

def rev_codon(codon):
    rev_comp = ""
    for i in rev_seq(codon):
        rev_comp = rev_comp + (complement_seq(i))
    return rev_comp

# print reverse complement of condon using above functions
seq = 'ATG'
print(rev_codon(seq))
