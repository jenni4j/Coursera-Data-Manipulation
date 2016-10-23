import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(doc):
  doc_id = doc[0]
  doc_text = doc[1]
  tokens = doc_text.split()

  for token in tokens:
    mr.emit_intermediate(token, doc_id)

def reducer(text, doc_ids):
  mr.emit((text, list(set(doc_ids))))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
