from collections import defaultdict
import numpy as np
import math

input_text = open('rosalind_ba10k.txt').read().split("--------\n")
epoch = int(input_text[0].strip())
text = input_text[1].strip()
all_character = input_text[2].split()
all_hidden = input_text[3].split()

transition = np.zeros([len(all_hidden), len(all_hidden)])
for h1, i in enumerate(input_text[4].split('\n')[1:]):
    for h2, j in enumerate(i.split()[1:]):
        transition[h1][h2] = float(j)

emission = []
for i in input_text[5].split('\n')[1:]:
    dic = {}
    for c, j in zip(all_character, i.split()[1:]):
        dic[c] = float(j)
    emission.append(dic)
for _ in range(epoch):
    forward = np.zeros([len(text), len(all_hidden)])
    for i, t in enumerate(text):
        for i1, _ in enumerate(all_hidden):
            if i > 0:
                for i2, _ in enumerate(all_hidden):
                    forward[i][i1] += forward[i - 1][i2] * transition[i2][i1]
            else:
                forward[i][i1] += 1
            forward[i][i1] *= emission[i1][t]

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
    pistar = forward * backward

    pistarstar = np.zeros([len(text), len(all_hidden), len(all_hidden)])
    for i, t in enumerate(text[:-1]):
        for i1, _ in enumerate(all_hidden):
            for i2, _ in enumerate(all_hidden):
                pistarstar[i][i1][i2] = forward[i][i1] * backward[i + 1][i2] * \
                    transition[i1][i2] * \
                    emission[i2][text[i + 1]] / np.sum(pistar[i])

    for i, _ in enumerate(text):
        pistar[i] = pistar[i] / np.sum(pistar[i])

    transition = np.sum(pistarstar, 0)
    for i, t in enumerate(transition):
        transition[i] = t / np.sum(t)

    temp_emis = []
    for c in all_character:
        filter_c = np.array(list(text)) == c
        print('fs', filter_c, np.sum(pistar[filter_c], 0))
        temp_emis.append(np.sum(pistar[filter_c], 0))
    temp_emis = np.array(temp_emis).transpose()

    print('t', temp_emis)
    emission = [dict() for i in range(len(all_hidden))]
    for i, e in enumerate(temp_emis):
        for c, j in zip(all_character, e):
            emission[i][c] = j / np.sum(e)
    print(emission)

print(" ".join(all_hidden))
for h1, tt in zip(all_hidden, transition):
    print(h1, " ".join([str(round(i, 3)) for i in tt]))

print("--------")

print(" ".join(all_character))
for h1, tt in zip(all_hidden, emission):
    print(h1, " ".join([str(round(i, 3)) for i in tt.values()]))
