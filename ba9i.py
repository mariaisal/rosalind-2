with open('rosalind_ba9i_output.txt', 'w') as out:
  with open('rosalind_ba9i.txt', 'r') as f:
    s = f.readline()
    cyclic_rotations = []
    for i in range(len(s)):
      cyclic_rotations.append(s[i:] + s[:i])
    sorted_cyclic_rotations = sorted(cyclic_rotations, key=lambda x: x[0])

    cyclic_rotations.sort()

    # print(''.join([ss[-1] for ss in cyclic_rotations]))

    out.write(''.join([ss[-1] for ss in cyclic_rotations]))