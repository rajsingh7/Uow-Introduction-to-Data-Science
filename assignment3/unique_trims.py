import MapReduce
import sys


"""
Problem 5

Consider a set of key-value pairs where each key is sequence id
and each value is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....

Write a MapReduce query to remove the last 10 characters from
each string of nucleotides, then remove any duplicates generated.

Map Input

Each input record is a 2 element list [sequence id, nucleotides]
where sequence id is a string representing a unique identifier
for the sequence and nucleotides is a string representing a sequence
of nucleotides

Reduce Output

The output from the reduce function should be the unique trimmed
nucleotide strings.

You can test your solution to this problem using dna.json:

$ python unique_trims.py data\dna.json

You can verify your solution by comparing your result with the file unique_trims.json.
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: sequence id
    # value: nucleotides sequence
    key = record[0]
    value = record[1][:-10]
    mr.emit_intermediate(1, value)

def reducer(key, list_of_values):
    # key: dummy
    # values: trimmed sequences
    unique = []
    for v in list_of_values:
        if v not in unique:
            unique.append(v)
    for u in unique:
        mr.emit(u)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
