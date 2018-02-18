from Bio import SeqIO
from Bio.SubsMat.MatrixInfo import blosum62

INF = 1000000000
protiens = []
with open('rosalind_glob.fasta', 'r') as f:
  for record in SeqIO.parse(f, 'fasta'):
    protiens.append(record.seq)
x, y = protiens

dp = [[-INF for i in range(len(y)+1)] for j in range(len(x)+1)]

dp[0][0] = 0

for i in range(len(x) + 1):
  for j in range(len(y) + 1):
    if i == 0 and j == 0:
      continue

    if i <= 0:
      a = -INF
    else:
      a = dp[i-1][j] - 5

    if j <= 0:
      b = -INF
    else:
      b = dp[i][j-1] - 5

    if i <= 0 or j <= 0:
      c = -INF
    elif (x[i-1], y[j-1]) in blosum62:
      c = dp[i-1][j-1] + blosum62[(x[i-1], y[j-1])]
    else:
      c = dp[i-1][j-1] + blosum62[(y[j-1], x[i-1])]
      
    dp[i][j] = max(a, b, c)

with open('rosalind_glob_output.txt', 'w') as out:
  out.write(str(dp[len(x)][len(y)]))