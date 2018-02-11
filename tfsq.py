from Bio import SeqIO
from io import StringIO

with open('rosalind_tfsq.txt', 'w') as out:
  handle = StringIO("")

  SeqIO.convert("tfsq.fastq", "fastq", handle, "fasta")

  out.write(handle.getvalue())