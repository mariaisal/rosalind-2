def join(l, sep):
  out = ''
  for element in l:
    out += str(element) + sep
  if len(sep) > 0:
    return out[:-len(sep)]
  return out

def euler_path(graph, vertices):
  # sum in-degree and out-degree
  indegree = dict.fromkeys(vertices, 0)
  outdegree = dict.fromkeys(vertices, 0)
  for vertex in vertices:
    if vertex in graph:
      outdegree[vertex] = len(graph[vertex])
      for adj in graph[vertex]:
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

      nextv = graph[v].pop()
      outdegree[v] -= 1
      v = nextv
    else:
      circuit.append(v)
      v = current_path.pop()
  # print(current_path, circuit)
  circuit.reverse()
  return circuit
  
with open('rosalind_ba3j_output.txt', 'w') as out:
  paired_read = []
  with open('rosalind_ba3j.txt', 'r') as f:

    k, d = f.readline().strip().split(' ')
    for line in f:
      x, y = line.strip().split('|')
      paired_read.append((x, y))
  
  vertices = set()
  G = {}
  for x, y in paired_read:
    fN = (x[:-1], y[:-1])
    sN = (x[1:], y[1:])
    vertices.add(fN)
    vertices.add(sN)

    if fN in G: 
      G[fN].append(sN)
    else:
      G[fN] = [sN]

  path = euler_path(G, list(vertices))
  xs = join([path[0][0]] + [x[int(k)-2:] for x, y in path[1:]], '')
  ys = join([path[0][1]] + [y[int(k)-2:] for x, y in path[1:]], '')
  print(xs, ys, d)
  out.write(xs[:int(d) + int(k)] + ys)
  
