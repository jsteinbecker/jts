

input = [[1,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,0],
         [0,0,0,0,0,0,0,0,0],
         [0,1,9,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]
         
def findNextCellToFill(grid, i, j):
        for x in range(i,9):
                for y in range(j,9):
                        if grid[x][y] == 0:
                                return x,y
        for x in range(0,9):
                for y in range(0,9):
                        if grid[x][y] == 0:
                                return x,y
        return -1,-1

def isValid(grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(9)])
        if rowOk:
                columnOk = all([e != grid[x][j] for x in range(9)])
                if columnOk:
                        # finding the top left x,y co-ordinates of the section containing the i,j cell
                        secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
                        for x in range(secTopX, secTopX+3):
                                for y in range(secTopY, secTopY+3):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False

def solveSudoku(grid, i=0, j=0):
        i,j = findNextCellToFill(grid, i, j)
        if i == -1:
                return True
        for e in range(1,10):
                if isValid(grid,i,j,e):
                        grid[i][j] = e
                        if solveSudoku(grid, i, j):
                                return True
                        # Undo the current cell for backtracking
                        grid[i][j] = 0
        return False

shift = ["MI","7C","7P","S","OP","EI","EP","3","N"]



solveSudoku(input,0,0)
for x in input:
        print(x)
#[[5, 1, 7, 6, 9, 8, 2, 3, 4], 
# [2, 8, 9, 1, 3, 4, 7, 5, 6], 
# [3, 4, 6, 2, 7, 5, 8, 9, 1], 
# [6, 7, 2, 8, 4, 9, 3, 1, 5], 
# [1, 3, 8, 5, 2, 6, 9, 4, 7], 
# [9, 5, 4, 7, 1, 3, 6, 8, 2], 
# [4, 9, 5, 3, 6, 2, 1, 7, 8], 
# [7, 2, 3, 4, 8, 1, 5, 6, 9], 
# [8, 6, 1, 9, 5, 7, 4, 2, 3]]

#[[5, 1, 7, 6, 8, 9, 2, 3, 4], 
# [2, 8, 9, 3, 7, 4, 1, 5, 6], 
# [3, 4, 6, 2, 1, 5, 7, 9, 8], 
# [6, 5, 2, 7, 9, 8, 4, 1, 3], 
# [1, 3, 8, 5, 4, 6, 9, 2, 7], 
# [9, 7, 4, 1, 2, 3, 6, 8, 5], 
# [4, 9, 5, 8, 6, 2, 3, 7, 1], 
# [8, 2, 1, 4, 3, 7, 5, 6, 9], 
# [7, 6, 3, 9, 5, 1, 8, 4, 2]]