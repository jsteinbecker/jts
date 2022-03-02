#%%
import yaml
from yaml import load, dump, Loader, Dumper
import pandas as pd


# %%
data = """
Rogue One:
    composer : GIACCHINO
    movements : 
        - Good Luck Little Sister *CT
        - Your Father Would Be Proud *CO

HTTYD- The Hidden World :
    composer : POWELL
    movements : 
        - With Love Comes a Great Waterfall *VN
"""


y = yaml.load(data ,Loader=Loader)
y
#%%
df = pd.DataFrame(y)
df = df.T
df
# %%
df = df.explode('movements')
df
# %%
list_of_composers = list(df.composer.unique())
list_of_composers

# %%
import re
# %%
df['movements'] = df['movements'].astype("str")
# %%
df['inst'] = df['movements'].str.extract("(\*\w\w)")
df['movements'] = df['movements'].str.replace("(\*\w\w)","",regex=True)
# %%
df
# %%
df.pivot(columns="composer",index="movements")

# %%
