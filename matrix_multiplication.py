from numpy import *

a1 = array([
    [1, 1],
    [1, 1]
])

a2 = array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 3, 3]
])

m = len(a1)
n = len(a1[0])
p = len(a2)
q = len(a2[0])

if n == p:
    print("Basic condition for matrix multiplication is met. Proceeding with multiplication")
    a3 = full((m, q), 0)
    for i in range(m):
        for j in range(q):
            for k in range(n):
                a3[i, j] += a1[i, k] * a2[k, j]
    print(a3)
else:
    print("Array sizes are not compatible for matrix multiplication. Array sizes are")
    print(m,"x", n, "and", p, "x", q )
