# -*- coding: utf-8 -*-
"""Monte Carlo 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UC6m-rNYQQX1sUJiKcZjU-MnZQ-qm9gs
"""

import numpy as np
import matplotlib.pyplot as plt

trials=1000
hits=0

a=2
b=3


x=[]
y=[]

sum=0
sum2=0

for i in range(trials):
    x=np.random.uniform(low=0,high=1)
    y=(x*np.exp(-x))

    sum=sum+y
    sum2=sum2+y**2

avg=(sum)/trials
avg2=(sum2)/trials

area=(b-a)*avg

error=((b-a)/np.sqrt(trials)) * (np.sqrt(avg2)-np.sqrt(avg)**2)

print(area,error)