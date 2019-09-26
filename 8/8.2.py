"""Questions
- directly lift code to read .code and .nuc?
- use enumerate function?
- split seq into codons using list generator?
"""

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

for i in range(n): # could use enumerate function here
    codon = b1[i] + b2[i] + b3[i]
    codons[codon] = aa[i]
    init[codon] = (st[i] == 'M')

# read sequence file
seq_file = 'anthrax_sasp.nuc'

file = open(seq_file)
seq = ""
for line in file:
    seq += line.strip()
file.close()

# translate input sequence using input codon table
trans = ""
curr_codon = ""
for i in range(len(seq)):
    curr_codon += seq[i]
    if (i + 1)%3 == 0:
        trans += codons[curr_codon.upper()]
        curr_codon = ""

print(f"Translation: {trans}")
print(f"Valid start codon: {init[seq[:3]]}")
