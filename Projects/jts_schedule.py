# %%
import numpy as np


# %%
grid = np.zeros((14,14))
grid[0][0:4] = -1
grid[1][4:11] = 8
grid[2][4:11] = 7
grid[6][3:11] = 3
grid [7][5:7] = -1
grid

# %%
def employeeview (empID):
   return grid[empID]
def dayview (dayID):
   d = grid.transpose()
   return d[dayID]
dayview(7)[8]

# %%
<<<<<<< HEAD
def week1count (e):
   count = 0
   emp1w = grid[e][0:7]
   for x in emp1w:
      if x != 0:
         count += 1
   return count
def week2count (e):
   count = 0
   emp1w = grid[e][7:14]
   for x in emp1w:
      if x != 0:
         count += 1
   return count
def checkweek (e):
   if week1count(e) < 5 and week2count(e) < 5:
      return True
   return False
checkweek(1)
    

# %%
=======
>>>>>>> e034a1bb2e21d10ac3e898eacf015babcfe2c57a
def countEmpShifts (empID):
   view = employeeview(empID)
   count = 0
   for x in view:
      if x > 0 or x == -1:
         count += 1
   return count

# %%
def AllEmpCount ():
   callEmpCount = []
   for x in range(14):
      c = countEmpShifts(x)
      callEmpCount.append(c)
   return callEmpCount
AllEmpCount()

# %%
empFTE = [7,7,8,7,8,8,8,7,8,8,5,5,8,8]
<<<<<<< HEAD

=======
>>>>>>> e034a1bb2e21d10ac3e898eacf015babcfe2c57a
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
<<<<<<< HEAD
trainedfor = [[0,1,2,3,4,5,6,7,8], 
=======
trainedfor = [[0,1,2,3,4,5,6,7,8],
>>>>>>> e034a1bb2e21d10ac3e898eacf015babcfe2c57a
              [0,1,2,3,4,5,6,7,8],
              [5,6,7,8],
              [5,6,7,8],
              [3,5,8],
              [0,1,2,3,4,5,6,7,8],
              [3],
              [0,1,2,4,5,6,7,8],
              [1,2],
              [0,1,2,3,4,5,6,7,8],
              [0,1,2,3,4,5,6,7,8],
              [0,1,2,3,4,5,6,7,8],
              [0,1,2,3,4,5,6,7,8],
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
<<<<<<< HEAD
=======


# %%
>>>>>>> e034a1bb2e21d10ac3e898eacf015babcfe2c57a
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
def noturnaround(e,d,s):
   if s>5 and d !=13:
      if grid[e][d+1] != 0:
         if grid[e][d+1] < 5:
            return False
   if s<4 and d !=0:
      if grid[e][d-1] !=0:
         if grid[e][d-1] > 5:
            return False
   return True

# %%
def solveCell (d,e,s):
   x = emptrained(e,s)
   y = notUnderFTE(e)
   z = shiftnotonday(d,s)
<<<<<<< HEAD
   m = checkweek(e)
   n = noturnaround(e,d,s)
   if x == True:
      if y == True:
         if z == True:
            if m == True:
               if n == True:
                  grid[e][d]=s
=======
   if x == True:
      if y == True:
         if z == True:
            grid[e][d]=s
>>>>>>> e034a1bb2e21d10ac3e898eacf015babcfe2c57a
   return False

# %%
x = 0
<<<<<<< HEAD
while x < 20000:
=======
while x < 10000:
>>>>>>> e034a1bb2e21d10ac3e898eacf015babcfe2c57a
   d =np.random.randint(0,14)
   e = np.random.randint(0,14)
   s = np.random.randint(0,9)
   if grid[e][d] == 0 and notUnderFTE(e) == True and noturnaround(e,d,s) == True:
      #print (grid[e][d],e,d,s,shiftnotonday(d,s),notUnderFTE(e))
      solveCell(d,e,s)
      x +=1
   else:
      x +=1
print(AllEmpCount(),cellswithShifts())
print(grid)

# %%
for x in grid.transpose():
   y = np.setxor1d(range(9),x)
   z = np.intersect1d(y,range(9))
   z


# %%
print("NCMC CPHT SCHEDULE | 2 WEEK")
print("-"*60)
new = ""
for i in range(len(grid)):
   myrow = ""
   for x in grid[i]:
      if x == 8:
         myrow += "N  "
      if x == 7:
         myrow += "3  "
      if x== 6:
         myrow += "EP "
      if x == 5:
         myrow += "EI "
      if x == 4:
         myrow += "S  "
      if x == 3:
         myrow += "7P "
      if x == 2:
         myrow += "7C "
      if x == 1:
         myrow += "MI "
      if x == 0:
         myrow += ".  "
      if x == -1:
         myrow += "pto"
   myrow += "| EMPLOYEE_NAME"
   new += myrow + "\n"
new += "-"*65

print(new)
print(cellswithShifts())

   
<<<<<<< HEAD


=======
>>>>>>> e034a1bb2e21d10ac3e898eacf015babcfe2c57a
