g = {}
vertices = set()
indegree = {}
outdegree = {}

def join(l, sep):
  out = ''
  for element in l:
    out += str(element) + sep
  return out[:-len(sep)]

def euler_path(graph, vertices):
  # sum in-degree and out-degree
  indegree = dict.fromkeys(vertices, 0)
  outdegree = dict.fromkeys(vertices, 0)
  for vertex in vertices:
    if vertex in g:
      outdegree[vertex] = len(g[vertex])
      for adj in g[vertex]:
        indegree[adj] += 1
  
  # determine start and end point
  start = -1
  end = -1
  for vertex in vertices:
    if indegree[vertex] < outdegree[vertex]:
      start = vertex
    elif indegree[vertex] > outdegree[vertex]:
      end = vertex

  print(start, end)

  # tour
  current_path, circuit, v = [start], [], start
  while len(current_path) > 0:
    if outdegree[v]:
      current_path.append(v)

      nextv = g[v].pop()
      outdegree[v] -= 1
      v = nextv
    else:
      circuit.append(v)
      v = current_path.pop()
  # print(current_path, circuit)
  circuit.reverse()
  return circuit

with open('rosalind_ba3g_output.txt', 'w') as out:
  with open('rosalind_ba3g.txt', 'r') as f:
    for line in f:
      nodes = line[:-1].split(' -> ')
      u = int(nodes[0])
      vs = [int(n) for n in nodes[1].split(',')]

      vertices.add(u)
      vertices = vertices  | set(vs)

      g[u] = vs
    
    path = euler_path(g, list(vertices))

    out.write(join(path, '->'))
