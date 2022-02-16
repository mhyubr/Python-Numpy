'''
Numpy digunakan untuk pengolahan array/matriks untuk sains komputasi

Install Numpy di Windows (connect internet):
pip install numpy
'''
import numpy as np # import modul numpy
a = np.array([1,2,3,4])
b = [1,2,3,4]
print(a)
print(b)

a += 1
# b += 1 # akan error karena 1 harus dijadikan list juga
b += [1]
print(a)
print(b)