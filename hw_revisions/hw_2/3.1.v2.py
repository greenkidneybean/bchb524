# input data: anthrax_sasp.nuc file
seq = "TTGAGTAGACGAAGAGGTGTCATGTCAAATCAATTTAAAGAAGAGCTTGCAAAAGAGCTAGGCTTTTATGA\
TGTTGTTCAGAAAGAAGGATGGGGCGGAATTCGTGCGAAAGATGCTGGTAACATGGTGAAACGTGCTATAGAAATTGC\
AGAACAGCAATTAATGAAACAAAACCAGTAG"

print(seq)

# does gene start with Met ("ATG") codon: bool
start_pos = seq.lower().find("agt") + 1

# return error if no start codon found
if start_pos == -1:
    print(f"Error: no Met codon found in sequence")
    exit()

# reading frame
frame = start_pos % 3

# length of gene
gene_seq = seq[start_pos-1:]
gene_length = len(gene_seq)

# amino acid length
aa_length = gene_length // 3

# gc content
g_cnt = gene_seq.lower().count("g")
c_cnt = gene_seq.lower().count("c")
percent_gc = ((g_cnt + c_cnt) / gene_length) * 100

# print statements
print(f"Start position(Met/'ATG'): {start_pos}")
print(f"Translation frame: {frame}")
print(f"Gene length: {gene_length}")
print(f"Amino acid length: {aa_length}")
print(f"Percent GC content: {percent_gc}")
print(f"Gene sequence: {gene_seq}")
