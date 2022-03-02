# %%
import numpy as np

"""
SCHEME
      GRID AXIS 0: EMPLOYEE
      GRID AXIS 1: DATE
      e for EMPLOYEE_ID
      d for DATE_ID
      s for SHIFT_ID

      0 is a cell that hasnt been assigned.
      1:8 are different shifts
      -1 is paid time off (pto)
"""

"""
#####################################
Basic Information / Data Generation
#####################################
"""

emp_names = "MONA AMANDA SABRINA MICHAEL STAR TRISHA BRIANNA TIFFANY BRITTANIE LEVI LINDA DANICA ESPERANZA JOSH LESLIE".split(" ")
print(emp_names[9])
empFTE = [7,7,8,8,8,8,8,8,8,8,8,8,8,5,2] # FTE Shifts for each employee

shift_names = ". MI 7C 7P S OP EI EP 3 N".split(" ")

# %% Setting select cells manually.
grid = np.zeros((len(emp_names),14))
grid[0][11:14] = 8
grid[0][0:4] = 8
grid[1][4:11] = 8
grid[2][4:11] = 7
grid[4][3:11] = 3
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
"""
Check Week: Verify not more than 4 shifts (40 hrs)
per week.
"""
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
def checkweek (e,d):
   if d < 7:
      if week1count(e) < 5:
        return True
   if d > 6:
      if week2count(e) < 5:
         return True
      else:
         return False

    

# %%
"""Checking FTE
Verify each employee is not assigned higer than their fte"""
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
   for x in range(len(emp_names)):
      c = countEmpShifts(x)
      callEmpCount.append(c)
   return callEmpCount
AllEmpCount()

# %%
def notOverFTE (e):
   if AllEmpCount()[e] < empFTE[e]:
      return True
   # for x in range(len(s)):
   #    if s[x] <= empFTE[x]:
   #       return True
   return False


# %%
"""Verify the assigned employee is trained for the
assigned shift"""

trainedfor = [[8], 
              [8],
              [7],
              [5,6,7,8],
              [3,5,8],
              [0,1,2,3,4,5,6,7],
              [0,1,2,3,4,5,6,7,8],
              [0,1,2,4,5,6,7,8],
              [0,1,3,4,5,6,7],
              [5,6,7,8],
              [0,1,2,3,4,5,6,7,8],
              [0,1,2,5,6,7],
              [0,1,2,5,6,7],
              [0,1,2,3,4,5,6,7],
              [0,1,2,3]]
# format:
# trainedfor[emp] = shifts that employee can work

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

def showMissShift (d):
   miss = [shift_names[int(x)] for x in dayview(5)]
   ms = set(shift_titles)-set(miss)
   ms = list(ms)
   return ms

# %%
"""Verifys an evening shift does not directly 
proceed a morning shift"""

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
def noOneDayGap (e,d):
   if 1 < d:
      if grid[e][d-1] == 0 and grid[e][d-2] > 0:
         return False
   if 12 > d:
      if grid[e][d+1] == 0 and grid[e][d+2] > 0:
         return False
   return True
# %%
def noSWeekend (d,s):
   if d in [0,6,7,13]:
      if s == 4:
         return False
   return True
# %%
def solveCell (d,e,s):
   x = emptrained(e,s)
   y = notOverFTE(e)
   z = shiftnotonday(d,s)
   m = checkweek(e,d)
   n = noturnaround(e,d,s)
   p = noSWeekend(d,s)
   if x and y and z and m and n and p:
      grid[e][d]=s
   return False

# %%
"""Run 20000 iterations of random possible shift assignments"""

x = 0
while x < 10000:
   d =np.random.randint(0,14)
   e = np.random.randint(0,len(emp_names))
   s = np.random.randint(0,9)
   if grid[e][d] == 0 and notOverFTE(e) == True and noturnaround(e,d,s) == True:
      #print (grid[e][d],e,d,s,shiftnotonday(d,s),notUnderFTE(e))
      solveCell(d,e,s)
      x +=1
   else:
      x +=1
print(AllEmpCount(),cellswithShifts())
print(grid)

for x in grid.transpose():
   y = np.setxor1d(range(9),x)
   z = np.intersect1d(y,range(9))
   z


shift_titles = '. MI 7C 7P S EI EP 3 N pto'.split(' ')

print("NCMC CPHT SCHEDULE | 2 WEEK")
print("-"*60)
new = ""
for i in range(len(grid)):
   myrow = ""
   for x in grid[i]:
      myrow  += shift_titles[int(x)]
      myrow += (3 - len(shift_titles[int(x)]))  * " "
   myrow += "|| "+ emp_names[i] + "(" + str(AllEmpCount()[i]) + ")"
   new += myrow + "\n"
new += "-"*65

print(new)
print(cellswithShifts())




for d in range (14):
   for s in range(9):
      if shiftnotonday(d,s):
         print (d, shift_titles[s])



# %%
for x in range(14):
   print(showMissShift(x))
# %%
