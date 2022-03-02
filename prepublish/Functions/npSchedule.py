import numpy as np
grid = np.zeros((9,14))
grid[1][2] = 5
grid[1][3] = 4
grid[1][5] = 8
grid
def employeeview (empID):
   return grid[empID]
def dayview (dayID):
   d = grid.transpose()
   return d[dayID]

def countEmpShifts (empID):
   view = employeeview(empID)
   count = 0
   for x in view:
      if x > 0:
         count += 1
   return count

def countDayShifts (dayID):
   view = dayview(dayID)
   count = 0
   for x in view:
      if x > 0:
         count += 1
   return count


