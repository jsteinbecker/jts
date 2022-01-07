def bigsci (s):
      no = int(s)
      L = len(str(no))
      SigFig = L - 1
      sig = "1"
      for x in range(0,SigFig):
            sig = sig + "0"
      disp = no / int(sig)
      disp = int(disp)
      disp = str(disp) + " *10^" + str(SigFig) 
      return disp

bigsci(2345634.88)
bigsci(77.8)