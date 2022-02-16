import numpy as np

# video ilustrasi kasus invers dan matrix
# https://www.youtube.com/watch?v=gMQwec7NBVY&list=PLZS-MHyEIRo6V6C2PHEx2Lt0hWIB_cL58&index=11

a = np.array([(1,-1),(1,1)])
print(a)

# invers matrix
a_inv = np.linalg.inv(a)
print(a_inv)
# pembuktain invers (jika dikali dot product akan menghasilkan matrix identitas)
print(np.dot(a,a_inv))

# determinan matrix
det_a = np.linalg.det(a)
det_a_inv = np.linalg.det(a_inv)
print(det_a)
print(det_a_inv)