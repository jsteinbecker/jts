from numpy import array


nermatrelvir_smiles = "CC1([C@@H]2[C@H]1[C@H](N(C2)C(=O)[C@H](C(C)(C)C)NC(=O)C(F)(F)F)C(=O)N[C@@H](C[C@@H]3CCNC3=O)C#N)C"
nermatrelvir_smiles

class chemj:
      def __init__(self,name,smiles):
          self.n = name
          self.sm = smiles

#--
x = chemj("nermatrelvir","CC1([C@@H]2[C@H]1[C@H](N(C2)C(=O)[C@H](C(C)(C)C)NC(=O)C(F)(F)F)C(=O)N[C@@H](C[C@@H]3CCNC3=O)C#N)C")
x.n
x.sm

ad = 741379/706434
ch_dth = 706/668
ad
excessChildMort = ch_dth/ad

import numpy as np
y = np.linspace(1,100,100)

list = []
for x in y:
      z = y[x-7:x]
      list.append(z)

list