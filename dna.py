
f = open("rosalind_dna.txt", "r")

s = f.readline()
a = 0
t = 0
c = 0
g = 0
for ch in s:
  if ch == 'A':
    a = a + 1
  if ch == 'T':
    t = t + 1
  if ch == 'C':
    c = c + 1
  if ch == 'G':
    g = g + 1

print a, c, g, t