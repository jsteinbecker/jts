data = open("/Users/joshsteinbecker/jts_project/Data/Music/Practice Logs/Feb2022/2022-02-12 PL.txt")
df = [x for x in data]
df.remove("\n")
df

import re
def mins (data):
   myliststr = []
   for x in data:
      myliststr.append(re.findall("\d*m\s",x))
   ints = []
   for x in myliststr:
      ints.append(re.findall("\d+",x))
   return ints


x = mins(df)