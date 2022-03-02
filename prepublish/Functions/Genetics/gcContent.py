def gcContent (seq):
   """Function: -> int --
   Return GC Content of Nucleic Acid Sequence. 
   Returned as decimal value. 
   
   >>> seq='accgtgacgtgtgacgtgccgtag'
   >>> gcContent(seq)
   'SCRIPT EXAMPLE':
        accgtgacgtgtgacgtgccgtag :
        G/C%: 0.625

   """
   
   seq = seq.lower()

   gcPerc = round((seq.count("g")+seq.count("c")) / len(seq),4)

   return gcPerc



if __name__ == '__main__':
   seq='accgtgacgtgtgacgtgccgtag'
   print(f'\nSCRIPT EXAMPLE:\n\t{seq} :')
   print(f'\tG/C%: {gcContent(seq)}\n')