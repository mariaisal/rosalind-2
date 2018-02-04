with open('rosalind_ba9j_output.txt', 'w') as out:
  end_with = []
  with open('rosalind_ba9j.txt', 'r') as f:
    end_with = list(f.readline())

  start_with = end_with
  for i in range(len(end_with) - 1):
    start_with = sorted(start_with)

    # print(start_with, end_with)

    start_with = [b + a for a, b in zip(start_with, end_with)]

  out.write(sorted(start_with)[0][1:] + '$')
  # out.write(''.join([ss[-1] for ss in cyclic_rotations]))