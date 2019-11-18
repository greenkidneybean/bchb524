import sys
from Bio.Blast import NCBIXML
from collections import OrderedDict
from operator import getitem

file = str(sys.argv[1])

result_handle = open(file)

hsp_dict = {}

for blast_result in NCBIXML.parse(result_handle):
    for alignment in blast_result.alignments:
        for hsp in alignment.hsps:
            print("Query:", blast_result.query)
            if hsp.expect < 1e-5:
                hsp_dict[blast_result.query] = {
                    'title':alignment.title,
                    'expect':hsp.expect, # evalue
                    'score':hsp.score, # score
                    'positives':hsp.positives,
                    'gaps':hsp.gaps
                }
                print('Match:', alignment.title)
                print('Score:', hsp.score)
                print('Evalue:', hsp.expect)
                print('Gaps:', hsp.gaps)
                print()
            else:
                print('***No matches with significant Evalue (1e-5)***')
                print()
        break

hsp_dict = OrderedDict(
    sorted(
        hsp_dict.items(),
        key = lambda x: getitem(x[1], 'score'),
        reverse=True)
    )

print("Most conserved gene based on HSP Score:")
print('Query gene:', list(hsp_dict.keys())[0])
print('DB match:', hsp_dict[next(iter(hsp_dict))]['title'])
print('Score:', hsp_dict[next(iter(hsp_dict))]['score'])
