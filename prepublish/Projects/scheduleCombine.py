# %%
import pandas as pd
import numpy as np
import random
# %%
df = pd.read_csv("/Users/joshsteinbecker/jts_project/Projects/schedexample.csv")
df

emplCt = len(df)
dayCt = 14
# %%
grid = np.zeros((emplCt,dayCt))
grid
# %%
def tf_emplLikesShift (e,s):
   "FUNCTION DETERMINES IF EMPLOYEE LIKES A PARTICULAR SHIFT"
   if len(df[df['prefers'].str.contains(s)][df['empl']==e]) > 0:
      return True
   return False
# %%
empl_fte_value = lambda e: int(df['fte'][df['empl'] == e])
# %%
def tf_underFTE (count, e):
   if count < empl_fte_value(e):
      return True
   return False

tf_underFTE(4,"JOSH")
# %%
[x for x in df[df['fte'] < 8]['empl']]
# %%
""" GET INDEX LIST OF ROWS THAT MEET A CERTAIN CONDITION """
index = df.index
condition = df['fte'] < 8
index[condition].tolist()
# %%
getEmpID = lambda x: df[df['empl']==x].index.tolist()[0]
getEmpID("JOSH")

# %%
getEmpName = lambda x: df['empl'][x]
getEmpName (16)
# %%
getEmpGrid = lambda x: grid[getEmpID(x)].tolist()
getEmpGrid("JOSH")
# %%
def getEmpShiftCt (e):
   count = 0
   for x in getEmpGrid(e):
      if 0 < x < 10:
         count += 1
   return count
# %%
getEmpFTE = lambda e: df['fte'][df['empl']== e].tolist()[0]

def tf_underFTE (e):
   if getEmpShiftCt(e) < getEmpFTE(e):
      return True
   return False
# %%
def solve (e,d,s):
   grid[e][d] = s
   if tf_underFTE(e) and tf_emplLikesShift(e):
      return True
   grid[e][d] = 0
   return False

solve(getEmpID("JOSH"),12,3)
# %%
