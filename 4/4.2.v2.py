# input data
seq = "AAAAAAAAAAAAAAAA"
num_rep = 4

# split the sequence (seq) by the number of repeats (num_rep)
tand_list = [seq[i:i+num_rep] for i in range(0,len(seq), num_rep)]

# check that seq can be equally divided by num_rep
if len(seq) % num_rep != 0:
    tand_list = tand_list[:-1]
    print(f"Note: sequence not equally divisible by repeat number input")

# function to check if all elements in list are equal
def equal_elements(list):
    return all(i == list[0] for i in list)

perfect_reps = equal_elements(tand_list)

# print statements
print(f"Input sequence: {seq}")
print(f"Input number of tandem repeats: {num_rep}")
print(f"List of tandem elements in sequence: {tand_list}")
print(f"Perfect tandem repeats in sequence: {perfect_reps}")
