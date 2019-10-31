import sys

primer_F = str(sys.argv[1])
primer_R = str(sys.argv[2])

primers = [primer_F, primer_R]

# reverse complement function
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

# print primers
print(rev_comp(primer_F))
print(rev_comp(primer_R))
