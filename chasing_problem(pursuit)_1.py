# -*- coding: utf-8 -*-
"""Chasing problem(pursuit) 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bYw5E_SBI6RrDDq8bDQTuUzVIUb3Hbzr
"""

import numpy as np

xt = [100, 110, 120, 129, 140, 149, 158, 168, 179, 188, 198, 209, 219]
yt = [0, 3, 6, 10, 15, 20, 26, 32, 37, 34, 30, 27, 23]

xd = [0]
yd = [60]
dist = 100

for t in range(12):
   dist = np.sqrt((xt[t]-xd[t])**2 + (yt[t]-yd[t])**2)
   print(dist)
   if(dist < 10):
     print("destroy target")
     break

   else:
    newxd = xd[t] + 20*(xt[t]-xd[t])/dist
    newyd = yd[t] + 20*(yt[t]-yd[t])/dist
    xd.append(newxd)
    yd.append(newyd)