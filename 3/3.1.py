#!/usr/bin/env python3
"""3.1 - Script to characterize a gene sequence from input file

Input: file that contains only the sequence, no headers

Output:
    Does gene start with Met ("ATG") codon: bool
    Does gene have a frame-1 Met codon: bool
    Length of gene: int
    Amino-acid length of gene: int
    GC content (%): float

Defaults:
    seq_file = "anthrax_sasp.nuc"
"""

import argparse
import os

# parse arguments
parser = argparse.ArgumentParser(
    description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument(
    "--seq_file",
    help="sequence file to be parsed",
    type=str,
    default="anthrax_sasp.nuc"
)
args = parser.parse_args()

# check that file exists and that there's something in it
if os.path.exists(args.seq_file):
    with open(args.seq_file) as f:
        seq = "".join(line.strip() for line in f)
    if seq == "":
        print(f"Error: {args.seq_file} is empty")
        exit()
else:
    seq = "TTGAGTAGACGAAGAGGTGTCATGTCAAATCAATTTAAAGAAGAGCTTGCAAAAGAGCTAGGCTTTTATGATGTTGTTCAGAAAGAAGGATGGGGCGGAATTCGTGCGAAAGATGCTGGTAACATGGTGAAACGTGCTATAGAAATTGCAGAACAGCAATTAATGAAACAAAACCAGTAG"
    print("Error: no input file found, defaulting to anthrax_sasp sequence \n")

# generate output

# Does gene start with Met ("ATG") codon: bool
start_index = seq.lower().find("agt")
if start_index == -1:
    print(f"Error: no Met codon found in sequence")
    exit()
print(f"Start index(Met/'ATG'): {start_index}")

# reading frame
frame = start_index % 3 + 1
print(f"Translation frame: {frame}")

# length of gene

# does NOT account for stop codons
#stop_codons = ['tag','taa','tga']
# maybe split the gene seq into codons and iterate through codons for stop
gene_seq = seq[start_index:]
gene_length = len(gene_seq)
print(f"Gene length: {gene_length}")

# amino acid lengt`h
aa_length = gene_length // 3
print(f"Amino acid length: {aa_length}")

# gc content
g_cnt = gene_seq.lower().count("g")
c_cnt = gene_seq.lower().count("c")
percent_gc = ((g_cnt + c_cnt) / gene_length) * 100
print(f"Percent GC content: {percent_gc}")

# gene sequence
print(f"Gene sequence: {gene_seq}")
