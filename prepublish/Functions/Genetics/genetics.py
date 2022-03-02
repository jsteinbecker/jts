import random
import re

def cleanDNA (seq:str):
   seq = seq.lower()
   seq = seq.replace(' ','')

   return seq
def gcContent (seq):
   """Function: Return GC Content of Nucleic Acid Sequence. Returned as decimal value. 
   """
   seq = seq.lower()

   gcPerc = round((seq.count("g")+seq.count("c")) / len(seq),4)

   return gcPerc
def ntCenter(seq,nts,displaytype = True):
    """FUNCTION WILL RETURN AN ARRAY WITH VALUES:
    
         - NUCLEOTIDE, 
         - AVERAGE POSITION IN CHAIN, AND 
         - % DISTANCE TO THE TRUE CENTER
    """
    centers = []

    for nt in nts:
        ind = []
        
        for i in range(len(seq)):
            if seq[i] == nt:
                ind.append(i)

        center = sum(ind)/len(ind)
        center = int(center)

        dist = round(((0.5 * len(seq)) - center) / len(seq),2)
        centers.append([nt,center,dist])

    if displaytype == True:
        out = ""
        for x in centers:

            print(f'{x[0]}: Center= {x[1]}, {int(x[2]*100)}% from true center')
            
    if displaytype == False:

        return centers
###############
# SINGLE OLIGO
###############
def randomOligo (length:int):
   """
   FUNCTION: Generate Oligonucleotide 
   with specified length.
   """
   base = 'acgt'

   # Loop to generate new base in sequence
   seq = ""
   for x in range(length):
      x = base[random.randint(0,3)]
      seq += x
   
   return seq
def rolig () -> str:
   length = int(input("Length (#bp): "))
   return randomOligo(length)

def randomOligoSet (length:int, qty:int):
   """
   FUNCTION: Generate set of oligos 
   of specified quantity and length
   """

   seqs = []
   for x in range(qty):
      x = randomOligo(length)
      seqs.append(x)
      
   return seqs
def roligs () -> list:
   length = int(input("Length (#bp): "))
   qty = int(input("Quantity: "))
   return randomOligoSet(length, qty)

def reverseSequence (seq: str):
   revs = seq[::-1]
   return revs

def mutate (seq,risk):
   mute = ""
   for x in seq:
      r = risk * 0.75
      score = random.random()
      if score < r:
         nt = 'acgt'
         nb = nt[random.randint(0,3)]
         mute += nb
      else: 
         mute += x
   return mute

class dnaseq (): 

   def __init__ (self, sequence: str):
      allowed = 'aAcCgGtTnNxXyY '
      self.seq = sequence
      self.rev = self.seq[::-1]

      def complement (seq):
         nt = 'acgtn'
         ntc = 'tgcan'
         compl = ""
         for b in seq:
            cid = nt.index(b)
            c = ntc[cid]
            compl += c
         return compl
      self.comp = complement(self.seq)

      self.len = len(self.seq)
      self.a = self.seq.count("a")
      self.c = self.seq.count("c")
      self.g = self.seq.count("g")
      self.t = self.seq.count("t")
      self.pur = self.a + self.g
      self.pyr = self.c + self.t
      self.gc = (self.g + self.c) / self.len

      def hydrogenbonds(seq):
         hb = 0
         for x in seq:
            if x == "g" or x == "c":
               hb += 3
            if x == "a" or x == "t":
               hb += 2
         return hb
      self.hbonds = hydrogenbonds(self.seq)


class mutationchain ():
   def __init__ (self, sequence, risk, generations):
      self.seq = sequence
      self.chain = [sequence]
      for x in range(generations):
         xn = mutate(self.chain[-1],risk)
         self.chain.append(xn)
      print(self.chain[-1])
      ch = 0
      for x in range(len(sequence)):
         if self.seq[x] != self.chain[-1][x]:
            ch += 1
      self.change = ch
      cd = []
      for x in range(1,len(self.chain)): 
         i = 0
         for y in range(len(self.chain[x])):          
            if self.chain[x][y] != self.chain[x-1][y]:
               i += 1
         cd.append(i)
      self.chaindiff = cd
