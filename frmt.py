from Bio import Entrez
from Bio import SeqIO
import numpy as np

Entrez.email = "nuttapat.kirawittaya@gmail.com"

with open('rosalind_frmt.txt', 'r') as f:
  s = f.readline()
s = s.split(' ');

handle = Entrez.efetch(db="nucleotide", id=s, rettype="fasta")

records = list (SeqIO.parse(handle, "fasta"))

# print [len(r.seq) for r in records]

argmin = np.argmin([len(r.seq) for r in records])

handle = Entrez.efetch(db="nucleotide", id=s[argmin], rettype="fasta")

print(handle.read())