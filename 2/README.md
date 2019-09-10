# Exercises 2.1 and 2.2

Michael Chambers - 190911

## Results

**Quickstart for 2.1.py:**
```
$ python 2.1.py   
gta
```

### **Quickstart for 2.2.py:**
```
$ python 2.2.py 
Codon position: 10
Translation Frame: 2
```

## Method
- 2.1
    - chains off of the codon string to reverse and use lower case text
- 2.2
    - run script by providing a query and a sequence to be searched
    - index of query: uses the `find()` function to search a string for first occurance of query
    - translation frame: divide index of query by 3 using `%` to acquire remainder, add 1
        - remainder 0 = frame 1
        - remainder 1 = frame 2
        - remainder 2 = frame 3
    - defaults run with the provided preliminary data and searches for "atg"

## Strengths
- it does the job
    - runs on default input data for hw assignment
    - returns codon position and translation frame values
- added argparse to guide use of script
- returns error if query not found within sequence

## Weaknesses
- cannot handle a file to be searched, would be a nice feature to add
- what if there are multiple queries found in the sequence and you want the index of all?

## Tests
- converts all input into a string (so can search for numbers in a number sequence)
- does NOT pass a seach with a different case (e.g. search "ATG" in "agtcgca")
    - look into using re (re.search(query, sequence, re.IGNORECASE))

## TODO:
- not case sensitive
- add option/kwargs for the `find()` function
- allow document to be searched