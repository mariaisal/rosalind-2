from Bio import SeqIO
from Bio.SubsMat.MatrixInfo import pam250

INF = 1000000000
protiens = []
with open('rosalind_loca.fasta', 'r') as f:
  for record in SeqIO.parse(f, 'fasta'):
    protiens.append(record.seq)
x, y = protiens

dp = [[0 for i in range(len(y)+1)] for j in range(len(x)+1)]
bt = [[0 for i in range(len(y)+1)] for j in range(len(x)+1)]

# dp[0][0] = 0

for i in range(len(x) + 1):
  for j in range(len(y) + 1):
    if i == 0 or j == 0:
      dp[i][j] = 0
      continue

    a = dp[i-1][j] - 5

    b = dp[i][j-1] - 5

    if (x[i-1], y[j-1]) in pam250:
      c = dp[i-1][j-1] + pam250[(x[i-1], y[j-1])]
    else:
      c = dp[i-1][j-1] + pam250[(y[j-1], x[i-1])]
      
    dp[i][j] = max(a, b, c, 0)
    if dp[i][j] == 0:
      bt[i][j] = 0
    elif dp[i][j] == a:
      bt[i][j] = 1
    elif dp[i][j] == b:
      bt[i][j] = 2
    elif dp[i][j] == c:
      bt[i][j] = 3

max_ = -INF
maxIndexI = -1
maxIndexJ = -1
for i in range(len(x) + 1):
  for j in range(len(y) + 1):
    if max_ < dp[i][j]:
      max_ = dp[i][j]
      maxIndexI = i
      maxIndexJ = j

i = maxIndexI
j = maxIndexJ
while bt[i][j] != 0:
  # print(i, x[i-1], j, y[j-1], dp[i][j])
  if bt[i][j] == 3:
    i -= 1
    j -= 1
  elif bt[i][j] == 2:
    j -= 1
  elif bt[i][j] == 1:
    i -= 1

# print(x[i:maxIndexI], y[j:maxIndexJ])
# print(dp)
with open('rosalind_loca_output.txt', 'w') as out:
  out.write(str(dp[maxIndexI][maxIndexJ]) + '\n')
  out.write(str(x[i:maxIndexI]) + '\n')
  out.write(str(y[j:maxIndexJ]) + '\n')