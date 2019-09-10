#!/usr/bin/env python3

import sys

query = sys.argv[1]
sequence = sys.argv[2]

# print codon position
value = str(sequence).find(str(query))
if value == -1:
    print(f'Error: "{query}" not found in sequence')
else:
    print(f"Codon position: {value}")

    # print translation frame
    frame = value % 3 + 1
    print(f"Translation Frame: {frame}")
