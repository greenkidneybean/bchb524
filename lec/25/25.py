import sys
from model import *

query = sys.argv[1]

if len(sys.argv) < 2:
    print("Input organism name")
    sys.exit(1)

def most_frequent(List):
    return max(set(List), key = List.count)

init()

condition = Name.q.name.contains(query)

id_list = []
for n in Name.select(condition):
    id_list.append(n.taxonomy.taxid)

try:
    child = most_frequent(id_list)
    print(f'TaxID best match for query: {child}')
except ValueError:
    print(f'Query "{query}" not found in database', file=sys.stderr)
    sys.exit(1)

child = Taxonomy.byTaxid(child)

parent = child
lineage = []
while parent.scientific_name != 'root':
    lineage.append(parent)
    parent = parent.parent

print(f'Ascending lineage for: {lineage[0].scientific_name}\n')

for i in lineage:
    print(f'{i.scientific_name} (TaxID: {i.taxid}) Rank: {i.rank}')
