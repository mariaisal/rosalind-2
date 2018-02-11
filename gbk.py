from Bio import Entrez

Entrez.email = "nuttapat.kirawittaya@gmail.com"

organ = "Aulogymnus"
st = "2003/04/14"
ed = "2012/05/28"

handle = Entrez.esearch(db="nucleotide", term='{0}[Organism] AND {1}:{2}[Publication Date]'.format(organ, st, ed))
record = Entrez.read(handle);

print(record['Count'])