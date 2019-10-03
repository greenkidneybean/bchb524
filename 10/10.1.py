import sys

seq = sys.argv[1]

dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
print("".join(map(lambda x: dict[x], list(seq.upper()[::-1]))))

# another short method without map
#print("".join({'A':'T','T':'A','G':'C','C':'G'}[i] for i in seq.upper()[::-1]))
