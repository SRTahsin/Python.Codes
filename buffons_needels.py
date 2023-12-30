# -*- coding: utf-8 -*-
"""Buffons Needels.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17SscaTE1ymT3WV-mLa4RDaoAyX9NqoGB
"""

# -*- coding: utf-8 -*-
"""011182095.ipynb

Automatically generated by Colabora
"""tory.

Original file is located at
    https://colab.research.google.com/drive/1ucmGLw9UBfsBfDVJFdVkvaQUw9YlHKA2

import numpy as np
import matplotlib.pyplot as plt

d=input("Enter d\n")
l=input("Enter l\n")
d=int(d)
l=int(l)

trials = 10000
hits = 0
hit_theta=[]
hit_D=[]
miss_theta=[]
miss_D=[]

for i in range(trials):
    D=np.random.uniform(low=0,high=d/2)
    theta=np.random.uniform(low=0,high=np.pi)

    if(D<= l/2*np.sin(theta)):
        hits+=1
        hit_theta.append(theta)
        hit_D.append(D)
    else:
        miss_theta.append(theta)
        miss_D.append(D)

estimated_pi=(l*trials)/hits
print(estimated_pi)

plt.scatter(hit_theta,hit_D,c='green')
plt.scatter(miss_theta,miss_D,c='red')
plt.show()