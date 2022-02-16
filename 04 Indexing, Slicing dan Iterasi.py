import numpy as np

a = np.arange(10)**2

print(a)

# mengambil nilai (indexing)
print(f"elemen ke 1 dari a adalah {a[0]}")
print(f"elemen ke 1 dari a adalah {a[6]}")
print(f"elemen ke 1 dari a adalah {a[-1]}")

# slicing 
print(f"elemen dari 1-6 adalah {a[0:5]}") # [start,end]
print(f"elemen dari 4 sampai akhir {a[3:]}")
print(f"elemen dari awal sampai 5 {a[:5]}")

# iterasi
for i in a:
    print(f"value = {i}") 