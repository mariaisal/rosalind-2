import random
from random import choice

with open('rosalind_ba2g.txt') as f:
    Dna = f.readlines()
Dna = [x.strip() for x in Dna]
y = Dna.pop(0)
tem = y.split()
k = int(tem[0])
t = int(tem[1])
n = int(tem[2])

Ctable = {'A': 0, 'C': 1, 'T': 2, 'G': 3}


def Score(motif):
    p = Profile(motif)
    score = 0
    for a in range(len(p)):
        score += (4 + t - max(p[a]))
    return score


def Motif(profile, dna):
    probMot = []
    i = 0
    for a in range(len(dna) - k + 1):
        sum = 1
        c = 0
        for b in range(i, i + k):
            sum *= (profile[c][Ctable[dna[b]]])
            c += 1
        i += 1
        probMot.append(sum)

    return probMot


def Profile(motif):
    p = []
    for i in range(len(motif[0])):
        for j in range(len(motif)):
            if j == 0:
                p.append([1, 1, 1, 1])
                p[i][Ctable[motif[j][i]]] += 1
            else:
                p[i][Ctable[motif[j][i]]] += 1
    return p


def Gibbs(dna, k, t, n):
    motif = []
    for j in range(0, t):
        i = random.randrange(0, len(dna[0]) - k + 1)
        motif.append(dna[j][i:i + k])
    bestMotif = list(motif)
    for j in range(0, n):
        i = random.randrange(0, t, 1)
        motif.pop(i)
        prof = Profile(motif)

        temp = Motif(prof, dna[i])
        print(temp)
        # motifi <- profile randomly generate
        idx = random.choices(list(range(0, len(dna[i]) - k + 1)), temp)

        motif.insert(i, dna[i][idx[0]:idx[0] + k])
        if Score(motif) < Score(bestMotif):
            bestMotif = list(motif)
    return bestMotif


answer = []
temp_motif = []
answer = Gibbs(Dna, k, t, n)
for i in range(0, 1):
    sample_motif = Gibbs(Dna, k, t, n)
    if Score(answer) > Score(sample_motif):
        answer = sample_motif
        print(answer, Score(answer))
for i in answer:
    print(i)

    # used global answer,temp_motif,Dna,y,tem,k,t,n