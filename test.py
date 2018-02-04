def MapLastToFirst(bwt):
  firstcol = sorted(bwt)
  map_index = []
  for eachchar in bwt:
    index = firstcol.index(eachchar)
    map_index.append(index)
    firstcol[index] = "#"
  return map_index
    
def BWMatching(firstcolumn, lastcolumn, pattern, last2first):
  top = 0
  bottom = len(lastcolumn) - 1
  while top <= bottom:
    if pattern:
      symbol = pattern[-1]
      pattern = pattern[:-1]
      last_short = lastcolumn[top : (bottom + 1)]
      if symbol in last_short:
        topIndex  = last_short.index(symbol) + top
        lastIndex = len(last_short) - last_short[::-1].index(symbol) + top - 1
        top    = last2first[topIndex]
        bottom = last2first[lastIndex]
      else:
        return 0
    else:
      return bottom - top + 1

def main(bwt, patterns):
  firstcol = sorted(bwt)
  last2first = MapLastToFirst(bwt)
  print(last2first)
  num_matchs = []
  for eachp in patterns:
    num_matchs.append(BWMatching(firstcol, bwt, eachp, last2first))
  print(" ".join(map(str, num_matchs)))

bwt = "TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC"
patterns = ["CCT", "CAC", "GAG", "CAG", "ATC"]
main(bwt, patterns)