import MapReduce
import sys

"""
Problem 4

The relationship "friend" is often symmetric, meaning that if I
am your friend, you are my friend. Implement a MapReduce algorithm
to check whether this property holds. Generate a list of all
non-symmetric friend relationships.

Map Input

Each input record is a 2 element list [personA, personB] where
personA is a string representing the name of a person and personB
is a string representing the name of one of personA's friends.
Note that it may or may not be the case that the personA is a
friend of personB.

Reduce Output

The output should be the full symmetric relation. For every pair
(person, friend), you will emit BOTH (person, friend) AND
(friend, person). However, be aware that (friend, person) may
already appear in the dataset, so you may produce duplicates if
you are not careful.

You can test your solution to this problem using friends.json:

$ python asymmetric_friendships.py data\friends.json

You can verify your solution by comparing your result with the
file asymmetric_friendships.json.

"""

mr = MapReduce.MapReduce()

def mapper(record):
    for i in range(len(record)):
        mr.emit_intermediate(record[i], record[1-i])

def reducer(key, list_of_values):
    # key: person
    # value: list of friends of that person
    for v in list_of_values:
        if list_of_values.count(v) == 1:
            mr.emit((key, v))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
