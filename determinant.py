import numpy as np

def isSingular(A):
    # singular if inverse exists
    # inverse -> if determinant is not zero
    return findDeterminant(A) == 0
    
def findDeterminant(A):
    if A.shape == (2, 2):
        a, b, c, d = tuple(A.ravel())
        return a*d - b*c
    else:
        n = len(A)
        s = 0
        for i in range(0, n):
            B = np.concatenate((A[1:, 0:i], A[1:, i+1:]), 1)
            s += ((-1)**i)*A[0][i]*findDeterminant(B)
        return s 
    