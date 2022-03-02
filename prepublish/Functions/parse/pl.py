import yaml
from yaml import Loader, Dumper
doc = open("Functions/parse/pl.yml").read()

d = """
s: [3,5,8]
s2 : [2,5,9]
"""
df = yaml.load(d,Loader=Loader)
z = []
for x in df['s']:
   for y in df['s2']:
      z.append((x,y,x+y))
for x,y,i in z:
   n = str(x)+"+"+str(y)+"="+str(i)
   print(n)

for x in range(enumerate(df['s'])):
   y = df['s'][x[0]] - df['s2'][x[0]]
   print(y)

x = (9,0)
x += x
x