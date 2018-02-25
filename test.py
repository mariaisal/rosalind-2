from collections import defaultdict
import numpy as np
import math

input_text = open('rosalind_ba10c.txt').read().split("--------\n")
text = input_text[0].strip()
all_character = input_text[1].split()
all_hidden = input_text[2].split()

transition = np.zeros([len(all_hidden), len(all_hidden)])
for h1, i in enumerate(input_text[3].split('\n')[1:]):
    for h2, j in enumerate(i.split()[1:]):
        transition[h1][h2] = float(j)

emission = []
for i in input_text[4].split('\n')[1:]:
    dic = {}
    for c, j in zip(all_character, i.split()[1:]):
        dic[c] = float(j)
    emission.append(dic)

forward = np.zeros([len(text), len(all_hidden)])
for i, t in enumerate(text):
    for i1, _ in enumerate(all_hidden):
        if i > 0:
            for i2, _ in enumerate(all_hidden):
                forward[i][i1] += forward[i - 1][i2] * transition[i2][i1]
        else:
            forward[i][i1] += 1
        forward[i][i1] *= emission[i1][t]
print(forward)

backward = np.zeros([len(text), len(all_hidden)])
rev_text = text[::-1]
for i, t in enumerate(text[::-1]):
    for i1, _ in enumerate(all_hidden):
        if i > 0:
            for i2, _ in enumerate(all_hidden):
                backward[i][i1] += backward[i - 1][i2] * \
                    emission[i2][rev_text[i - 1]] * transition[i1][i2]
        else:
            backward[i][i1] += 1

backward = np.flipud(backward)
print(backward)

prob = forward * backward
print(" ".join(all_hidden))
for i, _ in enumerate(text):
    print(" ".join([str(round(i, 4)) for i in (prob[i] / np.sum(prob[i]))]))
