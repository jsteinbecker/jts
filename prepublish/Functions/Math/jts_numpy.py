import numpy as np
####### NUMPY Functions

def getColumn (array:np.array, colID:int):
    """Return COLUMN from np.array and col_ID#
    >>> array [ : , colID ]
    >>> Note: colID is *zero-indexed* """

    return array[:,colID]

def getRow (array:np.array, rowID:int):
    """Return ROW from np.array and col_ID#
    >>> array [ rowID , : ]
    >>> Note: rowID is *zero-indexed* """
    
    return array[rowID,:]



def ex():
    arr = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
    c = getColumn(arr, 3)
    r = getRow(arr, 2)
    print(arr,"\ncol3: ",c,"\nrow2: ",r)
ex()