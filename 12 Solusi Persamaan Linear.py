import numpy as np

# video ilustrasi kasus persamaan linear:
# https://www.youtube.com/watch?v=6cfuKThXoVc&list=PLZS-MHyEIRo6V6C2PHEx2Lt0hWIB_cL58&index=12

# Kasus Pers. Linear ==> X * A = Y

# Diketahui :
A = np.array([(2,3),(1,2)])
Y = np.array([23,14])
print(A)
print(Y)

# Ditanyakan : X ?

# Penyelesaian :
A_inv = np.linalg.inv(A)
X = np.dot(A_inv,Y)
print(X)

# Cara Lain
X2 = np.linalg.solve(A,Y)
print(X2)