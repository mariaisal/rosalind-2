import numpy as np
import math

INF = 1000000000
str = ''
Observations = {}
States = []
Transition = [[]]
Emission = [[]]

with open('rosalind_ba10j.txt', 'r') as f:
  str = f.readline().strip()
  f.readline() # --------
  Observations = f.readline().strip().split()
  Observations = { Observations[i]:i for i in range(len(Observations)) }
  f.readline() # --------
  States = f.readline().strip().split()
  f.readline() # --------
  f.readline() # A   B
  Transition = np.zeros((len(States), len(States)))
  for i in range(len(States)):
    Transition[i,:] = [float(i) for i in f.readline().strip().split()[1:]]
  f.readline() # --------
  f.readline() # x   y   z
  Emission = np.zeros((len(States), len(Observations)))
  for i in range(len(States)):
    Emission[i,:] = [float(i) for i in f.readline().strip().split()[1:]]
  
Forward = np.zeros((len(States), len(str)))
Forward[:, 0] = Emission[:, Observations[str[0]]]
for j in range(1, len(str)):
  for i in range(len(States)):
    for k in range(len(States)):
      Forward[i, j] += Forward[k, j-1] * Transition[k, i] * Emission[i, Observations[str[j]]]

# print(Forward)

Backward = np.zeros((len(States), len(str)))
Backward[:, len(str) - 1] = 1 # Emission[:, Observations[str[0]]]
for j in range(len(str)-2, -1, -1):
  for i in range(len(States)):
    for k in range(len(States)):
      Backward[i, j] += Backward[k, j+1] * Transition[i, k] \
        * Emission[k, Observations[str[j+1]]]

# print(Backward)

Pr = Forward * Backward;

for i in range(len(str)):
  Sum = np.sum(Pr[:, i])
  for j in range(len(States)):
    Pr[j, i] /= Sum
# print(Pr)

with open('rosalind_ba10j_output.txt', 'w') as out:
  out.write("\t".join(States) + "\n")
  for i in range(len(str)):
    s = np.array2string(
      Pr[:, i],
      formatter={'float_kind':lambda x: "%.4f" % x},
      separator='\t',
      prefix=""
    )

    out.write(s[1:-1] + "\n")
    # print([str(round(x, 4)) for x in Pr[:, i]])
    # print("\t".join([str(np.round(x, 4)) for x in Pr[:, i]]))