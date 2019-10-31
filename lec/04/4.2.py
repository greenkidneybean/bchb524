#!/usr/bin/env python3
"""4.1 - Return number of tandem repeats

Script splits the input sequence by the input number of perfect tandem repeats and 
checks to see if the split string elements are equal to eachother.

Input:
    seq (str): sequence
    num_rep (int): number of perfect tandem repeats to look for in sequence

Output: presence and number of tandem repeats in sequence

Defaults:
    seq = "AAAAAAAAAAAAAAAA"
    num_rep = 4
"""

import argparse

parser = argparse.ArgumentParser(
    description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument(
    "--seq", 
    help="sequence to be checked for tandem repeats",
    type=str,
    default="AAAAAAAAAAAAAAAA"
)
parser.add_argument(
    "--num_rep", 
    help="number of perfect tandem repeats to check for within sequence",
    type=int,
    default=4
)
args = parser.parse_args()

# print input values
print(f"Input sequence: {args.seq}")
print(f"Input number of tandem repeats: {args.num_rep}")

# split the seq by num_repeats
tand_list = [args.seq[i:i+args.num_rep] for i in range(0,len(args.seq), args.num_rep)]

# check that seq can be equally divided by num_rep
if len(args.seq) % args.num_rep != 0:
    tand_list = tand_list[:-1]
    print(f"Note: sequence not equally divisible by repeat number input")
    
print(f"List of tandem elements in sequence: {tand_list}")

# check if all elements in list are equal
# could use the set() function and see if list reduced to single number
def equal_elements(list):
    return all(i == list[0] for i in list)

perfect_reps = equal_elements(tand_list)

print(f"Perfect tandem repeats in sequence: {perfect_reps}")