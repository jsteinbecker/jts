d = 0
l = 'SMTWRFS'
for x in range(1,32):
   d += 1
   day = l[d%7]
   print (f'{day} Jan {x}, 2022:')

l[8] 