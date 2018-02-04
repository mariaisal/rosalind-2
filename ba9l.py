def last2first(bwt):
  firstcol = sorted(bwt)
  map_index = []
  for eachchar in bwt:
    index = firstcol.index(eachchar)
    map_index.append(index)
    firstcol[index] = "#"
  return map_index

def bwtmatching(first, last, pattern, last_to_first):
  top = 0
  bottom = len(last) - 1
  while top <= bottom:
    if len(pattern) > 0:
      symbol = pattern[-1]
      pattern = pattern[:-1]
      last_short = last[top : (bottom + 1)]
      if symbol in last_short:
        topindex = last_short.index(symbol) + top
        bottomindex = len(last_short) - last_short[::-1].index(symbol) - 1 + top

        top = last_to_first[topindex]
        bottom = last_to_first[bottomindex]
      else:
        return 0
    else:
      return bottom - top + 1

with open('rosalind_ba9l_output.txt', 'w') as out:
  with open('rosalind_ba9l.txt', 'r') as f:
    last_column = list(f.readline().strip())
    first_column = sorted(last_column)

    last_to_first = last2first(last_column)
    print(last_to_first)

    patterns = f.readline().strip().split(' ')
    for pattern in patterns:
      out.write(str(bwtmatching(first_column, last_column, pattern, last_to_first)) + ' ')