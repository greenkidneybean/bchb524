from DNASeq_17 import *

def check_wiggle(cod, codon_dict):
    """Return AA residue to account 3rd position wiggle"""
    aa_list = []
    nuc_list = ['A','C','T','G']
    for i in nuc_list:
        try:
            aa_list.append(codon_dict[cod[:2]+i])
        except KeyError:
            pass
    aa_set = set(aa_list)
    if len(set_aa) == 1:
        return list(set_aa)[0]
    else:
        return 'X'

def check_codon(cod, codon_dict):
    """Returns AA reside "X" if "N" within codon"""
    if 'N' in cod.upper():
        return "X"
    else:
        try:
            return codon_dict[cod.upper()]
        except KeyError:
            print("Codon not found in codon dictionary")

def codon_dict(codon_file):
    """Convert codon table file to data dictionary

    Returns codon dictionary and start codon dictionary
    """
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
    start_codons = {}
    n = len(aa)

    for i in range(n):
        codon = b1[i] + b2[i] + b3[i]
        codons[codon] = aa[i]
        start_codons[codon] = (st[i] == 'M')
    return codons, start_codons

def translate_seq(seq, codon_dict):
    """Return AA sequence that accounts for codon wiggle"""
    aaseq = []
    codon_seq_len = (len(seq) // 3)*3
    for i in range(0,codon_seq_len, 3):
        codon = seq[i:i+3].upper()
        if codon[2].upper() == 'N':
            aa = check_wiggle(codon, codon_dict)
        else:
            aa = check_codon(codon, codon_dict)
        aaseq.append(aa)
    return "".join(aaseq)

def print_frame(seq, frame_num, codon_dict):
    if frame_num == 1:
        print(f"5'3' Frame 1: {translate_seq(seq, codon_dict)}")
    elif frame_num == 2:
        print(f"5'3' Frame 2: {translate_seq(seq[1:], codon_dict)}")
    elif frame_num == 3:
        print(f"5'3' Frame 3: {translate_seq(seq[2:], codon_dict)}")
    elif frame_num == 4:
        print(f"3'5' Frame 1: {translate_seq(rev_comp(seq), codon_dict)}")
    elif frame_num == 5:
        print(f"3'5' Frame 2: {translate_seq(rev_comp(seq)[1:], codon_dict)}")
    elif frame_num == 6:
        print(f"3'5' Frame 3: {translate_seq(rev_comp(seq)[2:], codon_dict)}")

def print_start(seq, start_codons):
    print(f"Valid start codon: {start_codons[seq[:3]]}")
