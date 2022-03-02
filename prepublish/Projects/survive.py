import random as r


   poss = r.choice([1,0,-1])

class creature:
   def __init__(self,n):
      self.name = 'creature' + str(n)
      self.x,self.y = r.randint(0,100), r.randint(0,100)
   def about(self):
      print (self.name,self.x,self.y)
   def move(self):
      self.x += r.choice([1,0,-1])
      self.y += r.choice([1,0,-1])
      return self.x,self.y

c = creature(1)
c.about()
c.move()
c.move()
c.about()
