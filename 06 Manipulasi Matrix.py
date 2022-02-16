import numpy as np
from numpy.lib.function_base import percentile

a = np.array((
            [1,2,3],
            [4,5,6]
            ))

print(f"matrix a dengan ukuran {a.shape}")
print(a)

# transpose
print("tranpose matrix dari a:")
print(a.transpose())
print(np.transpose(a))
print(a.T)

# flatten array, vector baris
print("flatten matrix a:")
print(a.ravel())
print(np.ravel(a))

# reshape
print("reshape matrix a:")
print(a.reshape(3,2))
print(a.reshape(6,1))
print(f"matrix a dengan ukuran {a.shape}")

# resize
print("reshape matrix a:")
a.resize(3,2)
print(a)
print(f"matrix a dengan ukuran {a.shape}")