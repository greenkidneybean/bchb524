# Exercise 3.1

Michael Chambers - 190916

## Results

```
$ python 3.1.py --seq_file anthrax_sasp.nuc
Start index(Met/'ATG'): 3
Translation frame: 1
Gene length: 177
Amino acid length: 59
Percent GC content: 39.548022598870055
Gene sequence: AGTAGACGAAGAGGTGTCATGTCAAATCAATTTAAAGAAGAGCTTGCAAAAGAGCTAGGCTTTTATGATGTTGTTCAGAAAGAAGGATGGGGCGGAATTCGTGCGAAAGATGCTGGTAACATGGTGAAACGTGCTATAGAAATTGCAGAACAGCAATTAATGAAACAAAACCAGTAG
```

## Method
- checks if input sequence file is empty, if so script will exit
- checks for start codon (MET/"ATG"), if not then script will break
- uses previous methods to get start index and reading frame number
- create new gene-sequence variable to calculate gene length, aa length, and gc-content

## Strengths
- it works!
- mild error checking (requires a non-empty sequence file and a start codon within the sequence)
- added a print of the gene sequence on which the length, aa length, and gc content is based
- defaults to run the anthrax_sasp.nuc file, but depends on that file being present
    - should embedd the anthrax sequence into the script

## Weaknesses
- expects a single sequence within a file (not a fasta file)
- does not check to see if input file is available
- does not check the gene sequence for stop codons within the translation frame
    - could implement by breaking gene sequence into list of codons then search each codon for stop match
    - in part with this, does not report a gene length that is divisible by 3, but does correct for aa length

## Tests
- raises error for empty file
- raises error for no start codon found in sequence

## What I learned
- thinking about the science/application (identifying the stop index is equally important)
- input files into script rather than straight string input

## TODO:
- add stop codon search
- handle a .fasta file?!