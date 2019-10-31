import sys

seq = str(sys.argv[1])

# functions
def rev(seq):
    """Return reverse sequence input"""
    return seq[::-1]

def comp(n):
    """Return complement of single nucleotide"""
    if n == "A":
        comp = "T"
    elif n == "T":
        comp = "A"
    elif n == "C":
        comp = "G"
    elif n == "G":
        comp = "C"
    else:
        comp = n
    return comp

def rev_comp(seq):
    """Return reverse complement of an input sequence"""
    rev_comp_seq = ""
    for i in rev(seq):
        rev_comp_seq = rev_comp_seq + (comp(i.upper()))
    return rev_comp_seq

def rev_palindrome(x):
    """checks if input sequence is a reverse palindrome"""
    y = len(x) // 2
    return x[:y].upper() == rev_comp(x)[:y]

print(rev_palindrome(seq))
