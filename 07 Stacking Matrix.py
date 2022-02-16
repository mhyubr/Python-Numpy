import numpy as np
from numpy.core.fromnumeric import amax
from numpy.matrixlib.defmatrix import bmat

a = np.array([1,2,3])
b = np.array([4,5,6])

aMat = np.zeros((2,3))
bMat = np.ones((2,3))

# stacking matrix, menumpuk matrix, menyatukan matrix

c = np.hstack((a,b)) # horizoantal stack
d = np.vstack((a,b)) # vertical stack

cMat = np.hstack((bMat,aMat))
dMat = np.vstack((bMat,aMat))

print(c)
print(d)
print(cMat)
print(dMat)