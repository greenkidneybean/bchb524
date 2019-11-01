

class DNASeq:
    def __init__(self,seq="",name=""):
        self.seq = seq.upper()
        self.name = name
    def read(self, filename):
        self.seq = ''.join(open(filename).read().split())
    def rev(self):
        return self.seq[::-1]
    def comp(self):
        d = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'N':'N'}
        return ''.join(map(d.get, self.seq))
    def rev_comp(self):
        return complement(self.rev)
    def length(self):
        return len(self.seq)
    def freq(self, nuc):
        return self.seq.count(nuc)
    def gc(self):
        gc_sum = self.freq('C') + self.freq('G')
        return 100 * float(gc_sum)/self.length()
