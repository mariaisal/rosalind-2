from Bio.Seq import translate

with open('rosalind_ptra.txt', 'r') as f:
    lines = []
    for i in f:
        lines.append(i.strip())

dna = lines[0]
tables = list(range(1, 7))
tables.extend(list(range(9, 16)))

for idx in tables:
    translated = translate(dna, table=idx).split('*')
    # print("".join(translated))
    if "".join(translated) == lines[1]:
        print(idx)
        break