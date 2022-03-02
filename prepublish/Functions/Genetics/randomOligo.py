import random

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

#######
# SETS
#######

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