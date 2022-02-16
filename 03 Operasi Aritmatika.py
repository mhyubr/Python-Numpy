import numpy as np

a = [1,2,3,4,5]
b = [6,7,8,9,10]

anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])


# ELEMENWISE operation / operasi per element array numpy
# penjumlahan dan pengurangan list python
hasil1 = a+b
# hasil2 = a-b # akan error karena list tidak dapat dikurangi
print(hasil1)
# print(hasil2)

# penjumlahan dan pengurangan array numpy
hasil1 = anp+bnp
hasil2 = anp-bnp
print(hasil1)
print(hasil2)

# operasi lain
hasil = anp*bnp
print(hasil)
hasil = anp/bnp
print(hasil)
hasil = anp**2
print(hasil)

cnp = np.array(([1,2,3],[4,5,6]))
dnp = np.array(([7,8,9],[-1,-2,-3]))
hasil = cnp + dnp
hasil = cnp * dnp
print(hasil)