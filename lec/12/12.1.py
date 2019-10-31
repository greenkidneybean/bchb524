from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

# functions
def aa_count(filename, filetype):
    res_dict = {}
    f = open(filename)
    for record in SeqIO.parse(f, filetype):
        temp_dict = ProteinAnalysis(str(record.seq)).count_amino_acids()
        for key, val in temp_dict.items():
            if key in res_dict:
                res_dict[key] = res_dict[key] + val
            else:
                res_dict[key] = val
    return res_dict

def print_results(data_name, data_dict):
    print(f"Results for {data_name}")
    print(f"Most frequent AA: {max(data_dict, key=data_dict.get)}")
    print(f"Least frequent AA: {min(data_dict, key=data_dict.get)}")
    print(f"Complete AA count:")
    for key, val in data_dict.items():
        print(key, val)
    print()

# generate aa count dictionaries for refseq and swissprot files
refseq = aa_count('human.protein.fasta', "fasta")
swissprot = aa_count('uniprot_sprot_human.dat', "swiss")

# print statements
print_results("RefSeq Human Proteins File ('human.protein.fasta')", refseq)
print_results("SwissProt Human Proteins File ('human.protein.fasta')", swissprot)
