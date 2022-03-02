import numpy as np
#%%
class schedule:

   def generate_grid(self):
      d = self.daycount - 1
      e = self.empl_count
      g = np.zeros((e,d),dtype="<U3")
      return g 

   def __init__(self):
      self.num = 0
      self.weekcount = 4
      self.daycount = self.weekcount * 7

      self.shift_titles = '. MI 7C 7P S EI EP 3 N pto'.split(' ')
      self.name_empls = 'MONA AMANDA SABRINA BRITTANIE BRIANNA TRISHA LEVI JOSH'.split(" ")
      self.empl_count = len(self.name_empls)
      
      self.grid = self.generate_grid()



   def shiftnotonday (self,d,s):
      if s in list(self.grid.T[d]):
         return False
      return True



# %%
s1 = schedule()

s1.grid[6][24] = "MI"
# %%
list(s1.grid.T[24])
s1.shiftnotonday(24,"7C")
# %%
