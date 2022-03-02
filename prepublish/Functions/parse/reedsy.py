import yaml
from yaml import Loader, Dumper
doc = open("/Users/joshsteinbecker/jts_project/Functions/parse/reed2a.yml").read()
dy = yaml.load(doc,Loader=Loader)
dy['seal_i']
rlist = [ "reed " + dy[x]['Reed'] for x in range(len(dy)) ]
type(dy)
