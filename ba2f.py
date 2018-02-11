from random import randint

def RandomSelectMotifs(Dna, k, t):
  Motifs = []
  for seq in Dna:
    index = randint(0, len(seq) - k)
    Motifs.append(seq[index:index+k])

  return Motifs

def Profile(Motifs, k):
  profile = []
  for i in range(k):
    for j in range(len(Motifs)):
      if j == 0:
        profile.append({ 'A': 1, 'T': 1, 'C': 1, 'G': 1 })
      profile[i][Motifs[j][i]] += 1
  return profile

def Motif(profile, Dna):
  Motifs = []
  for Seq in Dna:
    k = len(profile)
    maxProbs = -1
    kmer = ''
    for i in range(len(Seq) - k + 1):
      Sum = 1
      for j in range(k):
        Sum *= (profile[j][Seq[i+j]])
      if Sum > maxProbs:
        maxProbs = Sum
        kmer = Seq[i:i+k]
    Motifs.append(kmer)
  return Motifs

def Score(Motifs, k, t):
  profile = Profile(Motifs, k)
  score = 0
  for a in range(len(profile)):
    score += (4 + t - profile[a][max(profile[a], key=profile[a].get)])
    # print(profile[a][max(profile[a])], 4 + t, score)
  return score

def RandomizeMotifSearch(Dna, k, t):
  Motifs = RandomSelectMotifs(Dna, k, t)
  BestMotifs = list(Motifs)
  while True:
    profile = Profile(Motifs, k)

    Motifs = Motif(profile, Dna)
    if Score(Motifs, k, t) < Score(BestMotifs, k, t):
      BestMotifs = list(Motifs)
    else:
      return BestMotifs

with open('rosalind_ba2f.txt', 'r') as f:
  k, t = [int(x) for x in f.readline().strip().split(' ')]
  Dna = [x.strip() for x in f.readlines()]

  BestMotifs = RandomizeMotifSearch(Dna, k, t)

  for i in range(0, 1000):
    Motifs = RandomizeMotifSearch(Dna, k, t)
    if Score(Motifs, k, t) < Score(BestMotifs, k, t):
      BestMotifs = Motifs
      print(BestMotifs, Score(BestMotifs,k, t))
  # print(BestMotifs)
with open('rosalind_ba2f_output.txt', 'w') as out:
  for motif in BestMotifs:
    out.write(motif + '\n')