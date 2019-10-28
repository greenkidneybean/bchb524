# Exercise 16 - rework HW 5
import sys
import MyDNAStuff as mds

if len(sys.argv) < 3:
    print("Script requires codon table and sequence file as command-line input")
    sys.exit(1)

codon_file = sys.argv[1]
seq_file = sys.argv[2]

codon_dict, start_dict = mds.codon_dict(codon_file)
seq = mds.seq_from_file(seq_file)

for i in list(range(1,7)):
    mds.print_frame(seq, i, codon_dict)
    mds.print_start(mds.frame(seq, i), start_dict)
    mds.print_nuc_freq(mds.frame(seq, i))
    print()
