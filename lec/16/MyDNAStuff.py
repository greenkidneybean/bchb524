"""
Rework the lecture, and your solutions (or mine) from the homework exercises #1 through #3, to make a MyDNAStuff module.
Put as many useful nucleotide functions as possible into the module...

Rework the lecture, and your solutions (or mine) from homework exercises #4 and #5 to make the codon_table module with functions specified in this lecture.

Demonstrate the use of these modules to translate an amino-acid sequence in all six-frames with just a few lines of code.
The final result should look similar to Slide 10.
Your program should handle DNA sequence with N’s in it.
"""

def rev_comp(seq):
    """Returns the reverse complement of the input codon"""
    comp_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'N':'N'}
    return "".join([comp_dict.get(i.upper()) for i in seq[::-1]])

def check_wiggle(cod, codon_dict):
    """Return AA residue to account 3rd position wiggle"""
    check_aa = {}
    nuc_list = ['A','C','T','G']
    for i in nuc_list:
        check_aa[cod[:2]+i] = codon_dict.get(cod[:2]+i)
    set_aa = set(check_aa.values())
    if None in set_aa:
        return 'X'
    elif len(set_aa) == 1:
        return list(set_aa)[0]
    else:
        return 'X'

def check_codon(cod, codon_dict):
    """Returns AA reside "X" if "N" within codon"""
    if 'N' in cod.upper():
        return "X"
    else:
        return codon_dict[cod.upper()]

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

def seq_from_file(seq_file):
    """Read sequence file and return that sequence as a string"""
    file = open(seq_file)
    seq = "".join(file.read().split())
    file.close()
    return seq

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

def frame(seq, frame_num):
    """Return sequence reading frame"""
    if frame_num == 1:
        return seq
    elif frame_num == 2:
        return seq[1:]
    elif frame_num == 3:
        return seq[2:]
    elif frame_num == 4:
        return rev_comp(seq)
    elif frame_num == 5:
        return rev_comp(seq)[1:]
    elif frame_num == 6:
        return rev_comp(seq)[2:]

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

def nuc_freq(seq):
    """Convet input sequence to sorted list of nucleotide frequencies"""
    nuc_dict = {}
    for i in list(seq.upper()):
        if i not in nuc_dict.keys():
            nuc_dict[i] = 1
        else:
            nuc_dict[i] = nuc_dict[i] + 1
    sorted_list = sorted(nuc_dict.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_list

def print_nuc_freq(seq):
    """Print the sorted nucleotide list for a given sequence"""
    sorted_list = nuc_freq(seq)
    print("Nucleotide Frequency:")
    for i in sorted_list:
        print(f"{i[0]}: {i[1]} ")
