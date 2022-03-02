import re
import pandas as pd

class dailyPL :
   def __init__(self,inp):
      self.in_str = inp
      self.rawlist = praclog (self.in_str)
      self.rawlist = pl_rve_date (self.rawlist)
      self.date = getdate(self.in_str)
      self.len = len(self.rawlist)
      self.timeslist = gettime(self.rawlist)
      self.instlist = getinst(self.rawlist)
      self.cprlist = getcpr(self.rawlist)
      
      'to'

   def display (self):
      return self.date

   def praclog (x):
      x = re.sub("(?<=:\d\d)\s","\n",x)
      y = re.findall(".*(?<=:\d\d)(?=\n)",x)
      for i in y:
         if i == "":
            y.remove(i)
      return y

   def pl_rve_date (pl):
      e = re.findall("(?<=\s\d\d\d\d:).*", pl[0])[0].lstrip()
      pl.pop(0)
      pl.insert(0, e)
      return pl

   def getcpr (x):
      cpr = [re.findall("(?<=\().*(?=\))",i) for i in x]
      return cpr

   def getdate (str_):
      i = re.findall("\w*\s\d\d,\s\d\d\d\d",str_) 
      return i

   def gettime (list_):
      t = [re.findall("\d*:*\d+:\d\d", i)[0] for i in list_]
      return t

   def getinst (list_):
      ins = [re.findall("(?<=\s)\-\w\w(?=\s)", i) for i in list_]
      return ins


t ="January 22, 2022:   Epilogue- La La Land -EC (Hurwitz) 1:01:39 Bagatelle No. 1 0:12 Symphony No. 1 -CT (Brahms) 0:06 Ballad of Mesopotamia 0:06 Across the Stars 0:05 Battle of the Heroes 0:03 Der Erlkonig -VN (Ernst) 0:03 Daily Report 0:02 Candide -CL (Bernstein) 0:02 09 Clar 1--Candide 0:02 Tragic Overture -CO (Brahms) 0:02 Run Free -CT (Zimmer) 0:02 Katchaturian > Violin Concerto > D min... 0:02 Andante Festivo 0:01 Vitali Chaconne 0:01 503, Angels and Demons 0:01 Run Free 0:01 2 Serenades Op. 69 -VN (Sibelius) 0:01 Run Free 0:01"
t
pl = praclog(t)
pl.timeslist
cprs = getcpr(pl)
cprs
pl[0]
getdate(t)
for x in cprs:
   if x != []:
      print(x)

pl_rve_date(pl)

gettime(pl)

getinst(pl)

qpl = dailyPL(t)
qpl.timeslist

pf = pd.DataFrame((qpl.rawlist,qpl.timeslist,qpl.date*qpl.len,qpl.instlist),)
pf = pf.T
pf['work'] = pf[0]
pf[0]

str (["J","P"])