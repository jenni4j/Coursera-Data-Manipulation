import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(dna):
  dna_id = dna[0]
  dna_trimmed = dna[1][:-10].strip()
  mr.emit_intermediate(1, dna_trimmed)

def reducer(dna_id, nucleotides):
  unique_nucleotides = list(set(nucleotides))
  for nucleotide in unique_nucleotides:
    mr.emit(nucleotide)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
