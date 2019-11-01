# Functions
def complement_seq(seq):
        d = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'N':'N'}
        return ''.join(map(d.get, seq))

class DNASeq:
    def __init__(self,seq="",name=""):
        self.seq = seq.upper()
        self.name = name
    def read(self, filename):
        self.seq = ''.join(open(filename).read().split())
    def reverse(self):
        return self.seq[::-1]
    def complement(self):
        return complement_seq(self.seq)
