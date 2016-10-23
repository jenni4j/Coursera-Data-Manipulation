import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(line):
  line_id = line[1]
  mr.emit_intermediate(line_id, line)

def reducer(line_id, lines):
  orders = []
  for line in lines:
      if line[0] == 'order':
        orders = line
        lines.remove(line)
        break   
    
  for line in lines:
    mr.emit(orders + line)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)