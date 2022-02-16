import numpy as np

# data tunggal
a = np.floor(np.random.randn(1,6)*10) # floor untuk pembulatan | random.randn untuk random nilai

print(a)

print(f"\nnilai max dari a = {a.max()}")
print(f"posisi max dari a = {a.argmax()}")
print(f"nilai min dari a = {a.min()}")
print(f"posisi min dari a = {a.argmin()}")

print("\nmengurutkan nilai a:")
print(np.sort(a))
print("posisi yang ditukar:")
print(np.argsort(a))

print()
print()
print()

# data ganda
a = np.floor(np.random.randn(2,2)*10) # floor untuk pembulatan | random.randn untuk random nilai

print(a)

print(f"\nnilai max dari a = {a.max()}")
print(f"posisi max dari a = {a.argmax()}")
print(f"nilai min dari a = {a.min()}")
print(f"posisi min dari a = {a.argmin()}")

print("\nmengurutkan nilai a:")
print(np.sort(a))
print("posisi yang ditukar:")
print(np.argsort(a))

print()
print()
print()

# multitype data
dtipe = [('nama','S255'),('tinggi',int)]
data = [
    ('ucup',170),
    ('otong',150),
    ('mario',160)
    ]
a = np.array(data, dtype=dtipe)
print(f'{a}\n')
print(np.sort(a, order='tinggi'))
print(np.sort(a, order='nama'))
