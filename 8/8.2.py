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

# read sequence file
file = open(seq_file)
seq = "".join(file.read().split())
file.close()

# translate input sequence using input codon table
aaseq = []
for i in range(0,len(seq), 3):
    codon = seq[i:i+3]
    aa = codons[codon]
    aaseq.append(aa)

print(f"Translation: {''.join(aaseq)}")
print(f"Valid start codon: {init[seq[:3]]}")
