from numpy import save
from rdkit import Chem
from rdkit.Chem.rdmolfiles import MolFromSmiles
from rdkit.Chem import Draw
import yaml
from yaml import load, Loader

rawd = open('Functions/Chemistry/smilesData.yml','r')
rawd
data = rawd,yaml.load(rawd,Loader=Loader)
df =data[1]

n = [ x for x in df ]
s = [ x for x in df.values() ]

for x , y in df.items():
   mol = MolFromSmiles(y)
   dr = Draw.MolToImage(mol)
   dr.save("Functions/Chemistry/images/"+ x +".png")

