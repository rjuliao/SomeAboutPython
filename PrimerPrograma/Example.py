import numpy as np


name = input("Ingrese su nombre: ")
n = int(input("Ingrese dimensión de la matriz: "))
A = np.zeros((n,n))


for i in range(n):
    for j in range(n):
        A[i,j] = i*j*n

n = []

for k in range(len(name)):
    ab = name[k: k+1]
    n.append(ab)

print(A)
print()
print(n)