#!/usr/bin/env python3

import sys

codon = sys.argv[1]

print(str(codon)[::-1].lower())