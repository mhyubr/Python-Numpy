import numpy as np

# video ilustrasi kasus:
# https://www.youtube.com/watch?v=taHnC0WHXB8&list=PLZS-MHyEIRo6V6C2PHEx2Lt0hWIB_cL58&index=10
a = np.array([1,3]) # vector 2d
b = np.array([3,0]) # vector 2d

# perkalian dot
c = np.dot(a,b)
print(c)

# perkalian cross
a = np.array([1,2,0]) # vector 3d
b = np.array([2,1,0]) # vector 3d

c = np.cross(a,b)
print(c)