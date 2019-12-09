BCHB524 Final Project

Michael Chambers - 191220

Data:
- [Human RefSeq genome](https://www.ncbi.nlm.nih.gov/projects/genome/guide/human/index.shtml#download)
    - [human_protein.fa](ftp://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/annotation/GRCh38_latest/refseq_identifiers/GRCh38_latest_protein.faa.gz)
- [Yeast genome](https://www.ncbi.nlm.nih.gov/genome/?term=Saccharomyces%20cerevisiae[Organism]&cmd=DetailsSearch)
    - [yeast_proteins.fa](ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/146/045/GCF_000146045.2_R64/GCF_000146045.2_R64_protein.faa.gz)

Questions:
- what accession to use for query?
    - gi?
    - accession?
    - accession with version?
- what is the all-by-all?
    - align every protein to every other? (exhaustive)
    - search every protein against database and see what are hits? (only the cream)

IDEA:
- just pair the search down (quick script without database)
    - take query find what database it's in, search that database for hits
    - take those hits and search in reverse if it comes back to the query strain
- possible to get degrees of separation (leverages a database)
    - query gets a hit
    - that hit doesn't come back to the query, but it does come back to another protein that comes back to the query
    - would have to create a network graph
        - would have to be directional
        - graph made up only of particular e-values of significance (?)
    - search the database against itself (exclude self hits?)
        - find shorter paths
    - would need a node list with details and yeast/human designation

TODO:
- sketch using ribisome proteins yeast and dros
- blast align single seq to each seq in db
  - FIGURE OUT ONE-TO-ONE BLAST ALIGNMENT
- create db and keep all best matches if tied e value
- hedge bets on homologs: screen each of those hits in e-values and see if any of those point back to the current protein, then keep that one

REFS:
- [Biostars BLAST all-by-all](https://www.biostars.org/p/6541/)
- [Limit query to GI list](https://www.biostars.org/p/175478/)

Table:
query - reference - alignment - e-value - ortholog

use the "def lines" to identify orthologs


Results


Input:
- protein .fasta file
- expression optimization or changed sequence
  - this should be optional, second input sequence
- regions of interest
  - e.g. [55-60, 120-130, 67]

Output:
- list of 60bp oligos to be ordered
- skip the methionine (1st residue)
- number of changes
- number of potential residues

Methods:
- have a synonymous change parameter?
- generate fasta sequences for each change (60mer)
- do a blast alignment and cluster sequences in the same position

Strengths


Weaknesses


Tests


What I learned
