import numpy as np

INF = 1000000000
str = ''
Observations = {}
States = []
Transition = [[]]
Emission = [[]]

with open('rosalind_ba10k.txt', 'r') as f:
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
        Backward[i, j] += Backward[k, j+1] * Transition[k, i] * Emission[i, Observations[str[j+1]]]

  print(Forward)
  print(Backward)

  Pr = Forward * Backward;

  Pr_ = np.zeros([len(str), len(States), len(States)])
  for i in range(len(str) - 1):
    Sum = np.sum(Pr[:, i])
    for j in range(len(States)):
      for k in range(len(States)):
        Pr_[i, j, k] = Forward[j, i] * Backward[k, i+1] * Transition[j, k] * Emission[k, Observations[str[i+1]]] / Sum
    Pr[:, i] = Pr[:, i] / Sum;

  Transition = np.sum(Pr_, 0)
  for i in range(len(States)):
    Transition[i] = Transition[i] / np.sum(Transition[i])
  
  Emission = np.zeros((len(States), len(Observations)))
  for i in range(len(Observations)):
    f = np.array(list(str)) == Observations[i]
    Emission[:, i] = np.sum(Pr[f], 0)

  Emission = 
    

print(Pr)
print(" ".join(States))
for i in range(len(str)):
    print(" ".join([str(round(i, 4)) for i in (Pr[i] / np.sum(Pr[i]))]))