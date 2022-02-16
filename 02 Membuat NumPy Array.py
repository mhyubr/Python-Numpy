import numpy as np

# membuat vector
a = np.array([1,2,3,4])
b = np.array([1.5,2.5,5,6,7])

# membuat vector dengan range
c = np.arange(1,10,0.5)
d = np.arange(1,10,2)

# membuat linear space
e = np.linspace(1,10,4)

# array multidimensi / matrix
f = np.array([(1,2,3),(4,5,6)])

# matrix dengan nilai 0
g = np.zeros(5)
h = np.zeros((5,5))

# matrix dengan nilai 1
i = np.ones(5)
j = np.ones((5,5))

# matrix identitas
k1 = np.identity(5)
k2 = np.eye(5)

# display
print(a)
print(b)
print(c)
print(d)
print(e)
print(f+1) # matrix ditambah scalar 1
print(g)
print(h)
print(i)
print(j)
print(k1)
print(k2)