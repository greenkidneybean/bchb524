import sys
import xml.etree.ElementTree as ET

document = ET.parse(sys.argv[1])

root = document.getroot()
ns = '{http://uniprot.org/uniprot}'

for item in root.findall(f'./{ns}entry/{ns}reference'):
    key = item.attrib['key']
    for citation in item.findall(ns+'citation'):
        cit_dict = citation.attrib
        authors = ", ".join([ele.attrib['name'] for ele in citation.find(ns+'authorList')])
        if cit_dict['type'] == 'journal article':
            title = citation.find(ns+'title').text
            entry_type = cit_dict["type"].title()
            journal = f'{cit_dict["name"]} {cit_dict["volume"]} ({cit_dict["date"][:4]}): {cit_dict["first"]}-{cit_dict["last"]}'

            apa = f'{key}.  {entry_type}: {authors}. "{title}" {journal}'

            dbReference = citation.find(f'{ns}dbReference[@type="DOI"]')
            if dbReference is None:
                print(apa)
                print()
            else:
                doi = citation.find(f'{ns}dbReference[@type="DOI"]').attrib['id']
                print(apa, "DOI:", doi)
                print()
        else:
            print(f'{key}.  {cit_dict["type"].title()}: {authors}. Database Entry: {cit_dict["db"]}')
            print()
