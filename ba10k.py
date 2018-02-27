import numpy as np

INF = 1000000000
str = ''
Observations = {}
States = []
Transition = [[]]
Emission = [[]]

with open('rosalind_ba10k.txt', 'r') as f:
  epoch = int(f.readline().strip())
  f.readline() # --------
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

for _ in range(epoch):
  Forward = np.zeros((len(States), len(str)))
  Forward[:, 0] = Emission[:, Observations[str[0]]]
  for j in range(1, len(str)):
    for i in range(len(States)):
      for k in range(len(States)):
        Forward[i, j] += Forward[k, j-1] * Transition[k, i] * Emission[i, Observations[str[j]]]
    
  Backward = np.zeros((len(States), len(str)))
  Backward[:, len(str) - 1] = 1 # Emission[:, Observations[str[0]]]
  for j in range(len(str)-2, -1, -1):
    for i in range(len(States)):
      for k in range(len(States)):
        Backward[i, j] += Backward[k, j+1] * Transition[i, k] * Emission[k, Observations[str[j+1]]]

  Pr = Forward * Backward;

  Pr_ = np.zeros([len(str), len(States), len(States)])
  for i in range(len(str) - 1):
    Sum = np.sum(Pr[:, i])
    for j in range(len(States)):
      for k in range(len(States)):
        Pr_[i, j, k] = Forward[j, i] * Backward[k, i+1] * Transition[j, k] * Emission[k, Observations[str[i+1]]] / Sum
  for i in range(len(str)):
    Pr[:, i] = Pr[:, i] / Sum;

  Transition = np.sum(Pr_, 0)
  for i in range(len(States)):
    Transition[i] = Transition[i] / np.sum(Transition[i])
  
  Emission = np.zeros((len(States), len(Observations)))
  for i in Observations:
    f = np.array(list(str)) == i
    Emission[:, Observations[i]] = np.sum(Pr[:, f], 1)

  print(Emission)

  for i in range(len(States)):
    Emission[i] /= np.sum(Emission[i])
  print(Emission)
    

with open('rosalind_ba10k_output.txt', 'w') as out:
  out.write("\t" + "\t".join(States) + "\n")
  for i in range(len(States)):
    s = np.array2string(
      Transition[i],
      formatter={'float_kind':lambda x: "%.4f" % x},
      separator='\t',
      prefix=""
    )

    out.write(States[i] + "\t" + s[1:-1] + "\n")
  out.write("--------\n")
    
  out.write("\t" + "\t".join(Observations.keys()) + "\n")
  for i in range(len(States)):
    s = np.array2string(
      Emission[i],
      formatter={'float_kind':lambda x: "%.4f" % x},
      separator='\t',
      prefix=""
    )

    out.write(States[i] + "\t" + s[1:-1] + "\n")