from Bio import Entrez, SeqIO
from Bio.Blast import NCBIWWW, NCBIXML

Entrez.email = 'mjc346@georgetown.edu'

handle = Entrez.esearch(
    db='protein',
    term = '"Homo sapiens"[Organism] AND BRCA1[Gene Name] AND REFSEQ',
    usehistory='y'
)

result = Entrez.read(handle)

handle.close()

id_list = ','.join(result['IdList'])

handle = Entrez.efetch(
    db='protein',
    id=id_list,
    rettype='gb'
)

for gi,r in zip(result['IdList'], SeqIO.parse(handle, 'genbank')):
    print(f'\n*** START: {gi} ***\n')
    print('GI:', gi)
    print('Accession:', r.id)
    print('Description:', r.description)
    print(f"\nBLAST for GI {gi}...\n")

    result_handle = NCBIWWW.qblast(
        'blastp',
        'refseq_protein',
        gi,
        expect=1e-5,
        entrez_query='"Mus musculus"[Organism]'
    )

    for blast_result in NCBIXML.parse(result_handle):
        for desc in blast_result.descriptions:
            print('*** Alignment ***')
            print('Sequence:',desc.title)
            print('Evalue:', desc.e)
            print()

    file = f'blastp-np-{gi}.xml'
    save_file = open(file, 'w')
    save_file.write(result_handle.read())
    result_handle.close()
    print(f'*** END {gi} ***')
