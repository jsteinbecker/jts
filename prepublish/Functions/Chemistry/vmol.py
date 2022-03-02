
from rdkit import Chem
from rdkit.Chem.rdmolfiles import MolFromSmiles
from rdkit.Chem import Draw

import pandas as pd

file = pd.read_csv("/Users/joshsteinbecker/jts_project/Functions/Chemistry/smilesData.csv")
data = pd.DataFrame(file)
data

def vmol (mol_name):
   smiles = data.loc[data.MolName == mol_name, 'SMILES'].item()
   mol = MolFromSmiles(smiles)
   return Draw.MolToImage(mol).show() 


vmol("GWA")


def showmolnames():
   print(data.MolName)

showmolnames()