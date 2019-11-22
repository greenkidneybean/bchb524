import sys
import sqlite3

query = '%' + str(sys.argv[1]) +'%'

conn = sqlite3.connect('taxa.db3')
params = [query]
c = conn.cursor()
c.execute("""
    select * from name
    where name like ?
""", params)

id_set = {row[1] for row in c}

if len(id_set) == 0:
    print(f"Can't find query: {query}")
    sys.exit(1)

hits = []
for i in id_set:
    params = [i]
    c.execute("""
        select * from taxonomy
        where tax_id = ?
    """, params)
    for row in c:
        print(f'{row[1]} (taxid: {row[0]})')
