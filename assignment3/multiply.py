import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
  key = record[0]
  if key == 'A':
    mr.emit_intermediate(key, [record[1],record[2],record[3]])
  else:
    mr.emit_intermediate(key, [record[2],record[1],record[3]])

def reducer(key, list_of_values):
  A= {}
  B= {}

  if key == 'A':
    for v in list_of_values:
      A[(v[0], v[1])] = v[2]
    for u in mr.intermediate['B']:
      B[(u[0], u[1])] = u[2]
    for i in range(0,5):
      for j in range(0,5):
        if (i,j) not in A.keys():
          A[(i,j)] = 0
        if (j,i) not in B.keys():
          B[(j,i)] = 0
    result = 0

   for i in range(0,5):
     for j in range(0,5):
       for k in range(0,5):
         result = result + A[(i,k)]*B[(j,k)]
       mr.emit((i,j,result))
       result = 0

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
