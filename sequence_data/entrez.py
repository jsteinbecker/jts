# %%
from Bio import Entrez
from Bio import SeqIO
from Bio import Seq
import pandas as pd

class en_Seq:
    def __init__(self,acc_id,file,db):
        ent = pull_from_Entrez(acc_id, file, db)
        path = "sequence_data/"+file+".gb"
        self.seq = gb_to_Seq(path)
        self.feat = get_seq_features(self.seq)
        self.genes = get_seq_genes(self.seq)
        #self.aa_qty = aa_quantities(self.seq.translate())
        self.geneNames = get_gene_names(self.genes)
        self.loc_start = int(self.genes[-2].location.start)
        self.loc_end = int(sars2.genes[-2].location.end)
        self.translation = self.seq[self.loc_start:self.loc_end].translate()

def pull_from_Entrez (acc_id:str, filename:str, db:str):
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
def gb_to_Seq (gb_path):
    refseq = SeqIO.read(gb_path,"gb")
    return refseq
def get_seq_features (seq):
    features = seq.features
    return features
def get_seq_genes (seq):
    features = get_seq_features(seq)
    genes = []
    for f in features:
        if f.type == "gene":
            genes.append(f)
    return genes
def aa_quantities (aa_seq, sort=False):
    alphabet = "ACDEFGHIKLMNPQRSTVWY"
    df_a = []
    df_count = []
    for x in alphabet:
        df_a.append(x)
        df_count.append(round(aa_seq.count(x)/len(aa_seq)*100,3))
    df = pd.Series(perc,index=aa_resi)
    if sort == True:
        df = df.sort_values()
    return df
def nt_quantities (nt_seq):
    print ("NUCLEOTIDE COMPOSITION:")
    alphabet = "ACGT"
    nt = []
    perc = []
    for x in alphabet:
        nt.append(x)
        perc.append(round(nt_seq.count(x)/len(spike)*100,2))
    df = pd.Series(perc,index=nt)
    return df
def get_gene_names (genes):
    gene_names = []
    for f in genes:
        n = f.qualifiers['gene']
        gene_names.append(n)
    return gene_names


# prod = []
# for f in features:
#     if f.qualifiers == ['product']:
#         prod.append(f)
# prod

# %%
acc_num = "NC_045512.2"
pull_from_Entrez(acc_num, "SARSCOV2refseq", db="nucleotide")
mypath = "sequence_data/SARSCOV2refseq.gb"
myseq = gb_to_Seq(mypath)
myseqfts = get_seq_features(myseq)
mygenes = get_seq_genes(myseq)

#spike
mygenes[1]
# tx spike
spike = myseq.seq[21562:25384]
len(spike)
spikeAA = spike.translate()
aa_quantities(spikeAA,sort=True)
nt_quantities(spike)

# %%
sars2 = en_Seq(acc_num, "SARSCOV2refseq", db="nucleotide")
sars2.translation.seq
sars2.geneNames
# %%
