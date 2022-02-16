import numpy as np
from numpy.lib.function_base import iterable
 
#  membuat matrix dengan tipe data tertentu
a = np.array(([1,2,3],[4,5,6]), dtype=int)
print(a)
a = np.array(([1,2,3],[4,5,6]), dtype=float)
print(a)
a = np.array(([1,2,3],[4,5,6]), dtype=str)
print(a)
a = np.array(([1,2,3],[4,5,6]), dtype=bool)
print(a)

# membuat matrix dengan menggunakan function
def kuadrat(baris,kolom):
    return kolom**2
def jumlah(baris,kolom):
    return kolom + baris
b = np.fromfunction(kuadrat, (1,10), dtype=int)
c = np.fromfunction(jumlah, (4,4), dtype=float)
print(b)
print(c)

# membuat array atau matrix dengan menggunakan iterasi / iterable
iterable = (x*x for x in range(5)) # x**2 di setiap nilai range 1 - 4
d = np.fromiter(iterable, dtype=int)
print(d)

# multitype array
dtipe = [('nama','S255'),('tinggi',int)]
data = [
    ('ucup',150),
    ('otong',160),
    ('mario',180)
    ]
e = np.array(data, dtype=dtipe)
print(e)
print(e[0])