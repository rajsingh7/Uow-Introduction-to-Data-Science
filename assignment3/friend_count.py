import MapReduce
import sys

"""
Problem 3

Consider a simple social network dataset consisting of a set of
key-value pairs (person, friend) representing a friend relationship
between two people. Describe a MapReduce algorithm to count the
number of friends for each person.

Map Input

Each input record is a 2 element list [personA, personB] where
personA is a string representing the name of a person and personB
is a string representing the name of one of personA's friends.
Note that it may or may not be the case that the personA is a
friend of personB.

Reduce Output

The output should be a pair (person, friend_count) where person
is a string and friend_count is an integer indicating the number
of friends associated with person.

You can test your solution to this problem using friends.json:

$ python friend_count.py data\friends.json

You can verify your solution by comparing your result with the
file friend_count.json.
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: person
    # value: friend
    key = record[0]
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_values):
    # key: person
    # value: list of ones
    degree = 0
    for v in list_of_values:
        degree += v
    mr.emit((key,degree))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
