# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:50:58 2019

@author: Puneet Kochar
"""

import pandas as pd #imports python package called pandas.
import numpy as np #imports python package called numpy.
import matplotlib.pyplot as plt #imports plotting package of python
from sklearn.cluster import KMeans #imports Kmeans module from sci-kit learn package of python

customerLocations = pd.read_csv("customerLocations.csv",header=None,names=['x','y']) #reads the file into python with headers x and y


for k in range(1,21): #
    kmeans = KMeans(k).fit(customerLocations)#form clusters in between the range of 1 to 20 around customer locations
    clusterCenters = kmeans.cluster_centers_ #returns the coordinates of the each store location and store it as cluster centers.
    clusterMembership = kmeans.labels_ #assigns labels to each cu tomer based on the nearest store location.

    distanceCustomerToNearestStore={} #defines a dictionary to store the distance between customers and the nearest store.

    sumOfCustomerMarginalProfits = 0 #sets intital sum of all marginal profits for customers as 0.
    for customerNumber in range(0,10000):  
        customerXLocation = customerLocations['x'][customerNumber] #returns the location of each customer located east or west of the city center.
        customerYLocation = customerLocations['y'][customerNumber] #reutrns the location of each customer located north or south of city center.
        nearestStoreNumber = clusterMembership[customerNumber] #returns the nearest store number based on assigned labels of each customer
        nearestStoreXLocation = clusterCenters[nearestStoreNumber][0] #finds the nearest store location in the east or west of the city center.
        nearestStoreYLocation = clusterCenters[nearestStoreNumber][1] #finds the nearest store location in the north or south of the city center.
        #calculates the distance between the customer location and nearest store location
        distanceCustomerToNearestStore[customerNumber] = ((customerXLocation-nearestStoreXLocation)**2+(customerYLocation-nearestStoreYLocation)**2)**0.5

        profitForThisCustomer = 2000/(1+distanceCustomerToNearestStore[customerNumber]) #calculates the profit from each cutomer
        sumOfCustomerMarginalProfits += profitForThisCustomer # increases summ of all marginal profits with profits from each customers.

    costsOfOpeningStores = 200000*k #calculates the cost of opening stores.

    print('\n\nUsing '+str(k)+' stores we get a profit of:') #prints the string to console.
    totalProfit = sumOfCustomerMarginalProfits - costsOfOpeningStores # calculates total profit 
    print(totalProfit) #prints total profit to the console
    print('Sum of customer profits is:') #prints the string to the console.
    print(sumOfCustomerMarginalProfits) #prints the sum of all marginal profits.
    print('Cost of store openings is:') #prints string to the console.
    print(costsOfOpeningStores) #prints the cost of opening stores
    plt.scatter(k,totalProfit)
    plt.title("No. of stores opened vs total profit")
    plt.xlabel("The number of stores opened")
    plt.ylabel("Total Profit")

#part D
from sklearn import cluster
k =5 #number of clusters

kMeansResult = cluster.KMeans(k).fit(customerLocations)
kMeansResult.labels_
labelSymbols = ["*","+","o","s","^"]
labelColors = ['r','b','k','g','c']
 
for i in range(len(customerLocations)):
    groupNumber = kMeansResult.labels_[i]
    symbol = labelSymbols[groupNumber]
    col = labelColors[groupNumber]
    plt.scatter(customerLocations.loc[i,"x"],customerLocations.loc[i,"y"],marker=symbol,c=col)
   
    