reedset = []

class oboeReed:
   
   def __init__(self,):
      color = input('Color: ')
      staple = input('Staple: ')
      length = input('Length:')

      self.color = color
      self.staple = staple
      self.ilength = length
      self.len = length
      self.clips = []

      self.about = print (f'{self.color},{self.staple},\n\t{self.len},{self.clips}')

      reedset.append(self)

   def clip(self):
      amt = input('Clipped: ')
      if amt < 5:
         amount = amt
      if amt > 5:
         amount = self.len - amt
      self.clips.append(amount)
      self.len = self.len - amount