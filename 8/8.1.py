# input data
seq = 'ATGCATTCGTATTTTT'

# 3 ways to code dna complement
# 1. use the previous if statements
# 2. use two lists, maybe zip
# 3. use a dictionary
# 4. codon table?

# original method
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
    for i in rev_seq(seq):
        rev_comp = rev_comp + (complement_seq(i))
    return rev_comp

# two lists
def rev_comp_3(seq):
    nuc_list = ['a','t','c','g']
    trans_list = ['t','a','g','c']
    rev_comp = ""
    for i in seq[::-1]:


# dictionary
def rev_comp_3(seq):
    """Returns the reverse complement using dictionary"""
    trans_dict = {'a':'t', 't':'a', 'g':'c', 'c':'g'}
    rev_comp = ""
    for i in seq[::-1]:
        nuc = trans_dict[i.lower()]
        rev_comp = rev_comp + nuc
    return rev_comp
