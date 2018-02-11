import sys
from Bio import SeqIO
from Bio import motifs
from Bio.Alphabet import IUPAC

handle = open('rosalind_meme.fasta', "rU")
# records = list(SeqIO.parse(handle,'fasta'))
records = SeqIO.parse(handle,'fasta')
handle.close()

for record in records:
  print(record.seq)