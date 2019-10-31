import sys

codon_file = sys.argv[1]
seq_file = sys.argv[2]

# convert codon table file to data dictionary
file = open(codon_file)
data = {}
for line in file:
    split_line = line.split()
    key = split_line[0]
    value = split_line[2]
    data[key] = value
file.close()

b1 = data['Base1']
b2 = data['Base2']
b3 = data['Base3']
aa = data['AAs']
st = data['Starts']

codons = {}
init = {}
n = len(aa)

for i in range(n):
    codon = b1[i] + b2[i] + b3[i]
    codons[codon] = aa[i]
    init[codon] = (st[i] == 'M')

file = open(seq_file)
seq = "".join(file.read().split())
file.close()

# functions
def rev_comp(seq):
    """Returns the reverse complement of the input codon"""
    trans_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'N':'N'}
    return "".join([trans_dict[i.upper()] for i in seq[::-1]])

def check_wiggle(cod):
    check_aa = {}
    nuc_list = ['A','C','T','G']
    for i in nuc_list:
        check_aa[cod[:2]+i] = codons[cod[:2]+i]
    set_aa = set(check_aa.values())
    if len(set_aa) == 1:
        return list(set_aa)[0]
    else:
        return 'X'

def check_codon(cod):
    if 'N' in cod.upper():
        return "X"
    else:
        return codons[cod.upper()]

def translate_seq(seq):
    aaseq = []
    codon_seq_len = (len(seq) // 3)*3
    #print(codon_seq_len)
    #print(list(range(0,codon_seq_len, 3)))
    for i in range(0,codon_seq_len, 3):
        codon = seq[i:i+3].upper()
        #print(codon)
        if codon[2].upper() == 'N':
            aa = check_wiggle(codon)
            #print('wiggle')
            #print(aa)
        else:
            aa = check_codon(codon)
            #print('in table')
            #print(aa)
        aaseq.append(aa)
    return "".join(aaseq)

# print ORF AA sequences
print(f"5'3' Frame 1: {translate_seq(seq)}")
print(f"5'3' Frame 2: {translate_seq(seq[1:])}")
print(f"5'3' Frame 3: {translate_seq(seq[2:])}")
print(f"3'5' Frame 1: {translate_seq(rev_comp(seq))}")
print(f"3'5' Frame 2: {translate_seq(rev_comp(seq)[1:])}")
print(f"3'5' Frame 3: {translate_seq(rev_comp(seq)[2:])}")
