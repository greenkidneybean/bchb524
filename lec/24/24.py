from model import *
import sys

query = str(sys.argv[1])

condition = Name.q.name.contains(query)

id_set = set()
for n in Name.select(condition):
    id_set.add(n.taxID)

if len(id_set) == 0:
    print(f"Can't find query: {query}")
    sys.exit(1)

for i in id_set:
    sci_name = Taxonomy.get(i)
    print(f'{sci_name.scientificName} (taxid: {sci_name.id})')
