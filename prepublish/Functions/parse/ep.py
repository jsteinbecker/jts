import yaml
from yaml import Loader, Dumper
doc = open("Functions/parse/employees.yml").read()
dy = yaml.load(doc,Loader=Loader)

y = list(dy.keys())
y

ftes= [dy[x]['trained_for'] for x in dy.keys()]
fte= [*ftes]
fte
ftes = list(ftes)
type(ftes)
def containsS (el,s):
   return s in dy[el]['trained_for']
z = [containsS(x,"7C")for x in y].count(True)
z
   