fte = [7,
       7,
       8,
       8,
       8,
       8,
       8,
       8,
       5]

empWorksShifts = [[3,9], 
                  [2,9], 
                  [8], 
                  [8],
                  [0,1,2,3,4,5,6,7,8,9],
                  [0,1,2,3,4,5,6,7],
                  [4,5,6,7,8,9],
                  [5,6,7,8,9],
                  [1,2,3,4]]

grid = [[0,0,0,0,0,0,8,9,1,0,0,2,2,2],
        [0,1,2,3,0,0,0,0,0,0,0,2,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0],]

def countEmpShifts (employeeID):
   row = grid[employeeID]
   count = 0
   for x in row:
      if x > 0:
         count += 1
   return count
countallempSft = [countEmpShifts(x) for x in range(9)]
countallempSft 


def shiftOKwithEmployee (employeeID, shift):
   if shift in empWorksShifts[employeeID]:
      return True
   else:
      return False

def notOverFTE (employeeID):
   if countEmpShifts(employeeID) <= fte[employeeID]:
      return True
   else:
      return False

def countShiftsOnDay (dayID):
   count = 0
   for x in grid:
      if x[dayID] > 0:
         count += 1
   return count

def uniqueShiftsOnDay (dayID):
   shifts = []
   for x in grid:
      if x[dayID] != 0:
         if x[dayID] not in shifts:
            shifts.append(x[dayID])
         if x[dayID] in shifts:
            return False
      return True

#def uniqueShift (dayID):
day = []
for x in grid:
   for d in range(14):
      day.append(x[d])
day
grid

def isValid (employeeID, dayID, shift):
   stored = grid[employeeID][dayID]
   grid[employeeID][dayID] = shift
   check1, check2, check3 = shiftOKwithEmployee(employeeID,shift), notOverFTE(employeeID), uniqueShiftsOnDay(dayID) == True
   if all(check1, check2, check3) == True:
      return True
   else:
      grid[employeeID][dayID] = stored
      return False
      
def solve (grid):
   import random
   count = 0
   while count < 100:
      d = random.randint(0,13)
      e = random.randint(0,8)
      grid[e][d] = random.randint(0,8)
      count += 1
   return grid

try1 = solve(grid)
for x in try1:
   print(x)


# def runAllChecks (employeeID,dayID,shift):
#    c1 = notOverFTE(employeeID)
#    if c1 == True:
#       c2 = uniqueShiftsOnDay(dayID)
#       if c2 == True:
#          c3 = shiftOKwithEmployee (employeeID,shift)
#          if c3 == True:
#             return True
#          else:
#             return False
#       else:
#          return False
#    else:
#       return False

