def hasturnaround (row):
   amshifts = ['MI', '7C', '7P', 'S']
   pmshifts = ['EI', 'EP','3', 'N']

   r=[]
   for x in row:
      if x in amshifts:
         y = 0
      if x in pmshifts:
         y = 1
      else:
         y = -1
      r.append(y)
   ta = 0
   for x in range(1,len(r)):
      if r[x] == 0 and r[x-1] == 1:
         ta += 1
   if ta >= 1:
      return True
   else:
      return False

j = ". . . EI 7C S .".split(' ')
j
print(hasturnaround(j))
