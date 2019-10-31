# BCHB-524 Bioinformatics Computing (Python)

[Data for the course](http://edwardslab.bmcb.georgetown.edu/teaching/bchb524/2019/data/)
http://edwardslab.bmcb.georgetown.edu/teaching/bchb524/2019/data/

## Lecture topics and exercises:
00. BCHB-524 - Bioinformatics Computing Course Description
01. Introduction to Python - 1: Hello world, simple numbers
02. Introduction to Python - 2: Simple numbers, dna sequence
03. Introduction to Python - 3: Functions, if statement
04. Introduction to Python - 3: If and for statements
05. Introduction to Python - 3: DNA as a string
06. Introduction to Python - 3: Re-usable programs, handling input and output
07. Python Data Structures: Lists
08. Advanced Python Data Structures: Dictionaries, sets, files
09. Basic Python Review: Data structures
10. Advanced Python Idioms: Iteration, comprehensions, functional programming
11. Python Modules and Basic File Parsing: os, math, urllib, xml files
12. Sequence File Parsing using Biopython: Bio.SeqIO, Bio.SeqRecord
13. NGS Files and Pysam: Count reads, filter, SNPs
14. Protein Structure Informatics Using Biopython: Bio.PDB
15. XML Files and ElementTree: XML format, parse methods
16. Advanced Python Concepts: Modules
17. Advanced Python Concepts: Exceptions
18. Advanced Python Concepts: Object Oriented Programming

## Homework
* HW 1
    * 2.1 - Print Met codon backwards in lowercase
    * 2.2 - Find the position and translation frame of first start-codon in sequence
* HW 2
    * 3.1 - For anthrax gene: start codon in frame 1, nuc count, AA count, GC content
    * 4.1 - Compute reverse complement codon function
    * 4.2 - Check primer for tandem repeats
* HW 3
    * 6.1 - Compute reverse complement of a given NCBI Probe primer
    * 6.2 - Script that tests if reverse complement of primer is a palindrome
* HW 4
    * 8.1 - 3 ways to write a DNA reverse complement function
    * 8.2 - Script that takes a codon table and sequence and outputs the AA sequence
* HW 5
    * 9.1 - Modify DNA translation program (8.2) to translate in each forward and reverse frame, and handle "N" symbols in third position of a codon
    * 10.1 - Compact reverse complement function
    * 10.2 - Script that computes nucleotide frequencey using a dictionary
* HW 6
    * 11.1 - Read "data.csv" and compute mean, stdev for values of specific gene by group and all together
    * 12.1 - Get AA frequency for all genes in RefSeq and UniProt human proteome files and compare the two
* HW 7
    * 15.1 - Write program to print references from a UniProt.xml file
    * 16.1 - MyDNAStuff module to translate AA sequence in all 6 reading frames
* HW 8
    * 17.1 - Add try/except blocks to DNA and codon_table modules from lec 16
    * 18.1 - Convert modules for DNA seq and codon tables to classes, use classes to translate an AA sequence
