acc_num = "NC_045512.2"

from Bio import Entrez
from Bio import SeqIO
from Bio import Seq

Entrez.email = "joshsteinbecker@gmail.com"
handle = Entrez.efetch(db="nucleotide", id="NC_045512.2", rettype="gb", retmode="text")
file = open("/workspace/jts/Projects/sc2refseq.gb","w")

rec = handle.read()
rec
file.write(rec)
file.close()

refseq = SeqIO.read("/workspace/jts/Projects/sc2refseq.gb","gb")
len(refseq.seq)

features = refseq.features
len(features)
print(features)

genes = []
for f in features:
    if f.type == "gene":
        genes.append(f)
len(genes)

#spike
genes[1]
# tx spike
spike = refseq.seq[21562:25384]
len(spike)
spikeAA = spike.translate()

def aa_quantities ():
    alphabet = "ACDEFGHIKLMNPQRSTVWY"
    len(alphabet)
    for x in alphabet:
        print(x,round(spikeAA.count(x)/len(spike)*100,3),"%")
aa_quantities()

def nt_quantities ():
    print ("NUCLEOTIDE COMPOSITION:")
    alphabet = "ACGT"
    for x in alphabet:
        print(x,round(spike.count(x)/len(spike)*100,2),"%")
nt_quantities()


def get_gene_names ():
    gene_names = []
    for f in genes:
        n = f.qualifiers['gene']
        gene_names.append(n)
    return gene_names
get_gene_names()

prod = []
for f in features:
    if f.qualifiers == ['product']:
        prod.append(f)
prod