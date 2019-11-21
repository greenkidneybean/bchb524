import sys
import sqlite3

organism = '%' + str(sys.argv[1]) + '%'

conn = sqlite3.connect('taxa.db3')
params = [organism]
c = conn.cursor()
c.execute("""
    select name from name
    where name like ? and name_class = 'scientific name'
    limit 10;
""", params)
for row in c:
    print(row[0])
