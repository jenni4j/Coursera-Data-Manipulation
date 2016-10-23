import MapReduce
import sys
import collections

mr = MapReduce.MapReduce()
friendships = collections.defaultdict(list)

# =============================
# Do not modify above this line

def mapper(friend):
  person_name = friend[0]
  friend_name = friend[1]
  friendships[person_name].append(friend_name)
  mr. emit_intermediate(person_name, friend_name)

def reducer(person_name, person_friends):
  for person_friend in person_friends:
    if (person_name not in friendships[person_friend]):
      mr.emit((person_name, person_friend))
      mr.emit((person_friend, person_name))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
