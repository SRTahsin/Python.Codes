# -*- coding: utf-8 -*-
"""Serial_Chase.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1omOJM7aY6q-YgFQlLO3b_tPg5DmNch_r
"""

import numpy as np
import matplotlib.pyplot as plt

xa = [10]
ya = [0]

xb = [0]
yb = [10]

xd = [10]
yd = [10]

xc = [10]
yc = [10]

xd = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
yd = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


shoot = 0
d = 0
c = 0
b = 0

for t in range(21):
    dist = []
    dist1 = np.sqrt((xc[t] - xd[t]) * 2 + (yc[t] - yd[t]) * 2)
    dist.append(dist1)
    dist2 = np.sqrt((xb[t] - xc[t]) * 2 + (yb[t] - yc[t]) * 2)
    dist.append(dist2)
    dist3 = np.sqrt((xa[t] - xb[t]) * 2 + (ya[t] - yb[t]) * 2)
    dist.append(dist3)

    for i in range(3):
        if dist[i] < 5:
            shoot += 1
            if i == 0:
                print("c shot d")
                d += 1
            elif i == 1:
                print("b shot c")
                c += 1
            else:
                print("a shot b")
                b += 1

    newxc = xc[t] + 7 * (xd[t] - xc[t]) / dist[0]
    newyc = yc[t] + 7 * (yd[t] - yc[t]) / dist[0]
    xc.append(newxc)
    yc.append(newyc)

    newxb = xb[t] + 5 * (xc[t] - xb[t]) / dist[1]
    newyb = yb[t] + 5 * (yc[t] - yb[t]) / dist[1]
    xb.append(newxb)
    yb.append(newyb)

    newxa = xa[t] + 3 * (xb[t] - xa[t]) / dist[2]
    newya = ya[t] + 3 * (yb[t] - ya[t]) / dist[2]
    xa.append(newxa)
    ya.append(newya)

print(shoot)
print(f"d got shot {d} times")
print(f"c got shot {c} times")
print(f"b got shot {b} times")
plt.plot(xa, ya, xd, yd, xb, yb, xc, yc)
plt.show()