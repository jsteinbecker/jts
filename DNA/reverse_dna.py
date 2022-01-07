def reverse_dna (dna):
      l = []
      mydna = dna
      for n in mydna:
            l.append(n)
      rev = l[::-1]
      revstr = "".join(rev)
      print(revstr)