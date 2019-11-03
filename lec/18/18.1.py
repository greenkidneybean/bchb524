import sys
from DNASeq_18 import DNASeq
from codon_table_18 import codons

if len(sys.argv) < 3:
    print("Script requires codon table and DNA sequence input")
    sys.exit(1)

codons = codons().read(sys.argv[1])
seq = DNASeq().read(sys.argv[2])

for i in range(1,7):
    print(f"Frame {i}: {codons.translate(seq.get_frame(i))}")
