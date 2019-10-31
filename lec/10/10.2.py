import sys

seq_file = sys.argv[1]

file = open(seq_file)
seq = "".join(file.read().split())
file.close()

nuc_dict = {}
for i in list(seq.upper()):
    if i not in nuc_dict.keys():
        nuc_dict[i] = 1
    else:
        nuc_dict[i] = nuc_dict[i] + 1

sorted_list = sorted(nuc_dict.items(), key=lambda kv: kv[1], reverse=True)

for i in sorted_list:
    print(f"{i[0]}: {i[1]} ")
