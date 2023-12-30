# -*- coding: utf-8 -*-
"""K_means_Clust.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bgcieS5wQsxMf-u6qYwBebiUon_V-hbr
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
from math import sqrt

def load_data():
    data_path= '/content/drive/MyDrive/Colab Notebooks/jain_feats.txt'
    X = np.genfromtxt(data_path, delimiter=' ')

    data_path = '/content/drive/MyDrive/Colab Notebooks/jain_centers.txt'
    centroid_old = np.genfromtxt(data_path, delimiter=' ')
    return X, centroid_old

def ploting():
   # the Clustring points.
    c_index = 0
    ind=0
    while True:
        if c_index == len(clusters):
            break

        for i in clusters:
            temp_x = []
            temp_y = []
            for j in i:
                temp_x.append(X[j][0])
                temp_y.append(X[j][1])

            plt.scatter(temp_x, temp_y, s=10,  color="skyblue")
            c_index += 1



       #The Center points.
        temp_x = []
        temp_y = []
        for i in centroid_old:
            temp_x=(i[0])
            temp_y=(i[1])
            plt.scatter(temp_x, temp_y, marker='*', s=350, color="orange")
            ind+=1

        plt.show()

# function for getting eucledian distence
def  find_eucledian_dist(x , y):
   distance = 0.0
   for i in range(len(x)):
        distance += (x[i] - y[i]) ** 2
   return sqrt(distance)



# function for ploting clusters
def final_ploting():
   # the Clustring points.
    c_index = 0
    ind=0
    while True:
        if c_index == len(clusters):
            break
        colors = [ "Red","Green"]

        for i in clusters:
            temp_x = []
            temp_y = []
            for j in i:
                temp_x.append(X[j][0])
                temp_y.append(X[j][1])

            plt.scatter(temp_x, temp_y, s=10,  color=colors[c_index])
            c_index += 1



       #The Center points.
        temp_x = []
        temp_y = []
        for i in centroid_old:
            temp_x=(i[0])
            temp_y=(i[1])
            plt.scatter(temp_x, temp_y, marker='*', s=500, color=colors[ind])
            ind+=1

        plt.show()

#data loading

X, centroid_old = load_data()

ploting()



# Initialization
clusters = [ [], [] ]
eldist = 0
iteration = 0

while True:
    temp_clusters = [ [] , [] ]

    #cluster finding
    for i in range(len(X)):
        min_index = 0
        dist = []
        for j in range(len(centroid_old)):
            eldist = find_eucledian_dist(X[i],centroid_old[j])  #eucledian distance
            dist.append(eldist)
            min_index=dist.index(min(dist))
        #print(min_index)
        temp_clusters[min_index].append(i)
        #print(len(temp_clusters))

    #geting center
    centroid_new = []
    for L in temp_clusters:
    #determining average
        #print(L)
        avg=0
        for i in L:
            avg = avg + X[i]

        avg= avg / len(L)

        centroid_new.append(avg)


    if iteration >= 1000 :
        break
    else :
        for j in range(len(centroid_new)):
            c_dist = find_eucledian_dist(centroid_new[j],centroid_old[j])
            if c_dist < .0000001:
                break

    centroid_old = centroid_new
    clusters = temp_clusters.copy()         #assigning temp_cluster to clusters

    iteration +=1
print(centroid_old)
final_ploting()