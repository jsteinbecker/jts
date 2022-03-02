import pandas as pd

d = pd.read_csv("/Users/joshsteinbecker/jts_project/Data/AminoAcid_Data.csv")
df = pd.DataFrame(d)
df
x = df['three letter code']