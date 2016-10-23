import MapReduce
import sys

mr = MapReduce.MapReduce()


# =============================
# Do not modify above this line

def mapper(friend):
  person_name = friend[0]
  mr.emit_intermediate(person_name, 1)

def reducer(person_name, friend_count):
  mr.emit((person_name, sum(friend_count)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
