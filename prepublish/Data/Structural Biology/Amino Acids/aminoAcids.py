# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

# %%
df = pd.read_csv("/Users/joshsteinbecker/jts_project/Data/Structural Biology/Amino Acids/AminoAcid_Data.csv")
df

# %%
df['nlen'] = pd.Series([len(x) for x in df['full name']])
mass = df['average mass']

xyline = np.linspace(min(nlen),max(nlen),int(max(mass)))

# %% [markdown]
# ## Section: Meaningless Correlations
# With the provided dataset, draw a correlation that has no use or causal relationships with each other.

# %%
plt.figure(figsize=(7,7))
plt.grid(linewidth = 0.6)
# plt.scatter(mass,nlen, c=df["letter"])
groups = df.groupby("letter")
for name, group in groups:
    plt.plot(group["average mass"],group["nlen"], marker="o", linestyle="", label=name,markersize=4)
    plt.annotate(name,(group["average mass"],group["nlen"]),fontsize=15,ha='right')
# for x,y in zip(df["average mass"],df["nlen"]):
#    label = f'{df["letter"]}'
#    plt.annotate(label,(df['average mass'],df['nlen']))
#plt.legend()
plt.plot(xyline,linestyle='--',color='black',alpha=0.4)
plt.xlabel('MASS OF RESIDUE')
plt.ylabel('LENGTH OF RESIDUE NAME')
plt.annotate('Name Suggests a Smaller than True Mass',(50,5))
plt.annotate('Name suggests a Larger than true Mass',(0,12))
plt.title('MASS VS NAME LENGTH OF AMINO ACIDS',fontsize=18)
plt.show()

# %%
df.columns()




# %%
