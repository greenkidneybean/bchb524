class DNASeq:
    def __init__(self,seq="",name=""):
        self.seq = seq.upper()
        self.name = name
    def read(self, filename):
        self.seq = ''.join(open(filename).read().split()).upper()
        return self
    def rev(self):
        return self.seq[::-1]
    def comp(self):
        d = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'N':'N'}
        return ''.join(map(d.get, self.seq))
    def rev_comp(self):
        return ''.join(reversed(self.comp()))
    def length(self):
        return len(self.seq)
    def freq(self, nuc):
        return self.seq.count(nuc)
    def gc(self):
        gc_sum = self.freq('C') + self.freq('G')
        return 100 * float(gc_sum)/self.length()
    def get_frame(self, frame):
        assert frame in [1,2,3,4,5,6], "Not a valid frame number."
        if frame in [1,2,3]:
            return self.seq[frame-1:]
        else:
            return self.rev_comp()[frame-1:]
    def __str__(self):
        asstr = '>'+self.name+'\n'+self.seq
        return asstr
