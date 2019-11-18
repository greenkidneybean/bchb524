BCHB524 Final Project

Michael Chambers - 191220

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
