"""3 ways to code dna complement
1. use the previous if statements
2. use two lists, maybe zip
3. use a dictionary
4. codon table?
"""

# input data
seq = 'ATGCATTCGTATTTTT'

# method 1
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
def rev_comp_1(seq):
    rev_comp = ""
    for i in rev_seq(seq.upper()):
        rev_comp = rev_comp + (complement_seq(i))
    return rev_comp

# method 2
def rev_comp_2(seq):
    nuc_list = ['A','T','C','G']
    trans_list = ['T','A','G','C']
    rev_comp = ""
    for n in seq[::-1].upper():
        for x,y in zip(nuc_list, trans_list):
            if x == n:
                rev_comp += y
    return rev_comp

# method 3
def rev_comp_3(seq):
    """Returns the reverse complement using dictionary"""
    trans_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    rev_comp = ""
    for i in seq[::-1].upper():
        nuc = trans_dict[i]
        rev_comp = rev_comp + nuc
    return rev_comp

# method 4
def rev_comp_4(seq):
    """Returns the reverse complement of the input codon"""
    trans_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return "".join([trans_dict[i.upper()] for i in seq[::-1]])

# method 5
def rev_comp_5(seq):
    nuc_list = 'ATCG'
    trans_list = 'TAGC'
    rev_comp = ""
    for nuc in seq.upper()[::-1]:
        for x,y in enumerate(nuc_list):
            if y == nuc:
                rev_comp += trans_list[x]
    return rev_comp

# method 6
rev_comp_6 = "".join({'A':'T', 'T':'A', 'G':'C', 'C':'G'}[i] for i in seq.upper()[::-1])

# print results for functions
print(f"Input:    {seq}")
print(f"Method 1: {rev_comp_1(seq)}")
print(f"Method 2: {rev_comp_2(seq)}")
print(f"Method 3: {rev_comp_3(seq)}")
print(f"Method 4: {rev_comp_4(seq)}")
print(f"Method 5: {rev_comp_5(seq)}")
print(f"Method 6: {rev_comp_6}")
