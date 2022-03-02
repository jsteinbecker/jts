# %%
import numpy as np


# %%
grid = np.zeros((9,14))

grid

# %%
def employeeview (empID):
   return grid[empID]
def dayview (dayID):
   d = grid.transpose()
   return d[dayID]
dayview(7)[8]

# %%
def countEmpShifts (empID):
   view = employeeview(empID)
   count = 0
   for x in view:
      if x > 0:
         count += 1
   return count

# %%
def AllEmpCount ():
   callEmpCount = []
   for x in range(9):
      c = countEmpShifts(x)
      callEmpCount.append(c)
   return callEmpCount
AllEmpCount()

# %%
empFTE = [7,7,8,7,8,8,8,7,5]
def notUnderFTE (e):
   if AllEmpCount()[e] < empFTE[e]:
      return True
   # for x in range(len(s)):
   #    if s[x] <= empFTE[x]:
   #       return True
   return False

# %%
notUnderFTE(2)

# %%
trainedfor = [[0,1,2,3,4,5,6,7,8],
              [0,1,2,3,4,5,6,7,8],
              [5,6,7,8],
              [5,6,7,8],
              [3,5,8],
              [5,8],
              [0,1,2,4,5,6,7,8],
              [1,2],
              [0,1,2,3,4,5,6,7,8]]

# %%
grid[[5]]

# %%
def isTrainedFor ():
   val = []
   celllist = []
   for e in range(9):
      for x in employeeview(e):
         if x > 0:
            if x in trainedfor[e]:
               val.append("T")
            else:
               cell = f'emp={e},s={x}'
               celllist.append(cell)
               val.append("F")
         if x == 0:
            val.append("T")
   if val.count('F') == 0:
      return True
   else:
      return False, celllist
print(isTrainedFor())

# %%
def emptrained (e,s):
   if s in trainedfor[e]:
      return True
   else:
      return False

# %%
def countDayShifts (dayID):
   view = dayview(dayID)
   count = 0
   for x in view:
      if x > 0:
         count += 1
   return count

# %%


# %%
def cellswithShifts():
   count = 0
   for x in grid:
      for y in x:
         if y != 0:
            count += 1
   return count

# %%
def shiftnotonday (d,s):
   if s in dayview(d):
      return False
   return True

# %%
def solveCell (d,e,s):
   x = emptrained(e,s)
   y = notUnderFTE(e)
   z = shiftnotonday(d,s)
   if x == True:
      if y == True:
         if z == True:
            grid[e][d]=s
   return False

# %%
x = 0
while x < 100:
   d =np.random.randint(0,14)
   e = np.random.randint(0,9)
   s = np.random.randint(0,9)
   if grid[e][d] == 0 and notUnderFTE(e) == True:
      #print (grid[e][d],e,d,s,shiftnotonday(d,s),notUnderFTE(e))
      solveCell(d,e,s)
      x +=1
   else:
      x +=1
print(AllEmpCount(),cellswithShifts())
print(grid)

# %%

# %%



