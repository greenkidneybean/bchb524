"""
Questions:
- input from command line or prompt
- break-up by tumor group
- use other packages (numpy?)
- pull data file from class website?
"""

import sys
import csv
import math

data_file = sys.argv[1]
gene = sys.argv[2]

#data_file = 'data.csv'
#gene = 'R00884'

# functions
def calc_mean(int_list):
    return sum(int_list)/len(int_list)

def calc_stdev(int_list):
    mu = calc_mean(int_list)
    stdev = math.sqrt(sum([(i-mu)**2 for i in int_list])/(len(int_list)))
    return stdev

float(3)

# open file and gather gene data
f = open('data.csv')
rows = csv.DictReader(f, dialect='excel')
gene_data = []
for r in rows:
    gene_data.append(float(r[gene]))
f.close()

# compute mean and standard deviation
mean = calc_mean(gene_data)
stdev = calc_stdev(gene_data)

print(f'File: {data_file}')
print(f'Gene: {gene}')
print(f'Mean: {mean}')
print(f'Standard deviation: {stdev}')
