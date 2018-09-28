# python3
import numpy as np

V = 0
v = []
w = []
a = [int(x) for x in input().split()]
W = a[1]
n = a[0]

for i in range(a[0]):
    temp = 0
    for x in map(int, input().split()):
        if temp == 0:
            v.append(x)
            temp += 1
        else:
            w.append(x)

for i in range(n):
    if W == 0:
        break

    a = min(w[i], W)
    V = V + a*(v[i]/w[i])
    print(a)
    print(V)
