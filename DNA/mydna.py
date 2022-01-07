import re

class dnaSEQ:
#'''This ObjClass Holds a DNA Sequence'''
      def __init__(self,strseq):
          self.seq = strseq
          # Displays the DNA Sequence
          self.len = len(strseq)
          # Length of DNA Sequence as integer
          self.count_c = self.seq.count("c")
          self.count_g = self.seq.count("g")
          self.count_gc = self.count_g + self.count_c
          self.perc_gc = round(self.count_gc / self.len, ndigits= 3 )

      def has_orf (self):
      #'''This Function looks for a start codon'''
            if re.findall("atg",self.seq) == []:
                  return False
            else:
                  return True

      def percGC (self):
            
            gc = self.count_gc
            gcp = gc / self.len
            return gcp

      def about (self):
            print(f'SEQUENCE: {self.seq}\n   LENGTH: {self.len}\n   GC%: {self.perc_gc}')


def gc_content (dna):
# Fx Gives a GC% or GC%-Range for a DNA-Seq
# INPUT dna = string

      mydna = dna.lower() #string to lowercase

      gc = mydna.count("g") + mydna.count("c")
      t = len(mydna) # t total length of dna
      n = mydna.count("n") # n count of unspecified nts

      if mydna.rfind("n") == -1:
            # Standard: No "N" nucleotides
            perc = gc / len(mydna) * 100
            percent_gc = perc / 100
            out = (f'{mydna}\nGC#: {gc}/{t} \n     {perc}%\n ---------------------\n')
            return print(out)

      else:
            # GC Range: "N" nucleotides are present
            gcmin = gc / len(mydna) * 100
            gcn = gc + n
            gcmax = gcn / len(mydna) * 100
            out = (f'{mydna}\rGC#: {gc}-{gcn}/{t} \r    {gcmin}% - {gcmax}%\n ---------------------\n')
            return print(out)

