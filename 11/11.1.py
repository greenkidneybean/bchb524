import sys
import csv
import math

data_file = sys.argv[1]
gene = sys.argv[2]

# functions
def calc_mean(int_list):
    return sum(int_list)/len(int_list)

def calc_stdev(int_list):
    mu = calc_mean(int_list)
    stdev = math.sqrt(sum([(i-mu)**2 for i in int_list])/(len(int_list)))
    return stdev

def tumor_grps(grp, int_list):
    mean = calc_mean(int_list)
    stdev = calc_stdev(int_list)

    print(f'Tumor Group: {grp}')
    print(f'Mean: {mean}')
    print(f'Standard deviation: {stdev}')
    print()

# open file and gather gene data
f = open('data.csv')
rows = csv.DictReader(f, dialect='excel')

tumor_dict = {}

for r in rows:
    if r['TUMOUR'] in tumor_dict.keys():
        tumor_dict[r['TUMOUR']].append(float(r[gene]))
    else:
        tumor_dict[r['TUMOUR']] = [float(r[gene])]
f.close()

# print statements
print(f'File: {data_file}')
print(f'Gene: {gene}')
print()

# tumor groups
for key, val_list in tumor_dict.items():
    tumor_grps(key, val_list)

# all data
all_values = []
for i in tumor_dict.values():
    all_values = all_values + i
tumor_grps('All Values', all_values)
