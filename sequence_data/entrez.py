acc_num = "NC_045512.2"

from Bio import Entrez
from Bio import SeqIO
from Bio import Seq

def pull_from_Entrez (acc_id:str,filename:str,db:str):
    """
    acc_id:     ACCESSION NUMBER
    filename:   LOCATION FOR GENBANK FILE TO POPULATE
    db:         DATABASE (ex."nucleotide")
    """
    Entrez.email = "joshsteinbecker@gmail.com"
    handle = Entrez.efetch(db=db, id=acc_id, rettype="gb", retmode="text")
    file = open("sequence_data/"+filename+".gb","w")
    rec = handle.read()
    file.write(rec)
    file.close()

pull_from_Entrez(acc_num, "SARSCOV2refseq", db="nucleotide")

def gb_to_Seq (gb_path):
    refseq = SeqIO.read(gb_path,"gb")
    return refseq
mypath = "sequence_data/SARSCOV2refseq.gb"
myseq = gb_to_Seq(mypath)

def get_seq_features (seq):
    features = seq.features
    return features
myseqfts = get_seq_features(myseq)

def get_seq_genes (seq):
    features = get_seq_features(seq)
    genes = []
    for f in features:
        if f.type == "gene":
            genes.append(f)
    return genes
mygenes = get_seq_genes(myseq)

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