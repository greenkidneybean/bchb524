from codon_table_17 import *

def rev_comp(seq):
    """Returns the reverse complement of the input codon"""
    comp_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'N':'N'}
    try:
        nuc_list = [comp_dict[i.upper()] for i in seq[::-1]]
    except KeyError:
        print("Non-standard nucleotide identified in sequence.")
    return "".join(nuc_list)

def seq_from_file(seq_file):
    """Read sequence file and return that sequence as a string"""
    file = open(seq_file)
    seq = "".join(file.read().split())
    file.close()
    return seq

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
