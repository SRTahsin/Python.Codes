# -*- coding: utf-8 -*-
"""Random No.(2) 30/07/23.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wqv1zzR2Am9-G6XDRBQPEmkZg2X2L9W_
"""

import numpy as np
import matplotlib.pyplot as plt

n = 50
z = [9]
u = []
x =[]

for i in range(1,n+1):
    new_z = (2*z[i-1]**2 + 5*z[i-1]+6) % 20
    z.append(new_z)
    new_u = new_z / 20
    u.append(new_u)
    x.append(i)

print(z)
print(u)

plt.bar(x,u,color = "green")
plt.xlabel("iteration")
plt.ylabel("u value")
plt.show()