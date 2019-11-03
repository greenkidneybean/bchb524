class codons:
    def __init__(self,codon_table="", start_table=""):
        self.codon_table = codon_table
        self.start_table = start_table
    def read(self, filename):
        # function to read a codon table
        file = open(filename)
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

        self.codon_table = codons
        self.start_table = start_codons
        return self
    def get_aa(self, codon):
        # returns aa symbol for a given codon
        try:
            return self.codon_table[codon]
        except KeyError:
            print('No such codon found in codon table')
    def get_ambig_aa(self, codon):
        # codon with N's
        nucs = ['A','C','T','G']
        check_aa = set([self.codon_table.get(codon[:2]+i) for i in nucs])
        if None in check_aa:
            return 'X'
        elif len(check_aa) == 1:
            return list(check_aa)[0]
        else:
            return 'X'
    def start_codon(self, seq):
        # return True if seq starts with init codon
        try:
            codon = seq[:3]
            return self.start_table[codon]
        except KeyError:
            print('No such codon found in codon table')
    def translate(self, seq):
        # return aa seq for input dna seq
        trans_seq = []
        for i in range(0,((len(seq) // 3)*3), 3):
            codon = seq[i:i+3].upper()
            if "N" in codon:
                aa = self.get_ambig_aa(codon)
            else:
                aa = self.get_aa(codon)
            trans_seq.append(aa)
        return "".join(trans_seq)
