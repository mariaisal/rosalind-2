deBruijnGraph = {}
with open('rosalind_ba3e_output.txt', 'w') as out:
  with open('rosalind_ba3e.txt', 'r') as f:
    for line in f:
      fNode = line[:-2]
      sNode = line[1:-1]
      if fNode in deBruijnGraph:
        deBruijnGraph[fNode].append(sNode)
      else:
        deBruijnGraph[fNode] = [sNode]

  keys = deBruijnGraph.keys()
  keys.sort()
  for key in keys:
    deBruijnGraph[key].sort();
    out.write(key + ' -> ' + ','.join(deBruijnGraph[key]) + '\n')