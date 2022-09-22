from ast import Break
import math
from re import I
import numpy as np

def clusterAnalysis(reflectance):
    arr = np.zeros((np.size(reflectance),2))
    arr1 = np.zeros(0)
    arr2 = np.zeros(0)
    for index, x in enumerate(reflectance):
        arr[index][0] = x
    for i in range(np.shape(arr)[0]):
        if (i%2)==0:
            arr[i][1] = 1
        else:
            arr[i][1] = 2
    for i in range(np.shape(arr)[0]):
        if arr[i][1].astype(int) == 1:
            arr1 = np.append(arr1,arr[i][0])
        else:
            arr2 = np.append(arr2,arr[i][0])
    mean1 = np.mean(arr1)
    mean2 = np.mean(arr2)

    while True:
        arr1 = np.zeros(0)
        arr2 = np.zeros(0)
        for i in range(np.shape(arr)[0]):
            if np.greater(np.absolute(arr[i][0]-mean1), np.absolute(arr[i][0]-mean2)):
                arr[i][1] = 2
            else:
                arr[i][1] = 1
        for i in range(np.shape(arr)[0]):
            if arr[i][1].astype(int) == 1:
                arr1 = np.append(arr1,arr[i][0])
            else:
                arr2 = np.append(arr2,arr[i][0])
        new_mean1 = np.mean(arr1)
        new_mean2 = np.mean(arr2)
        if np.equal(mean1,new_mean1):
            break
        mean1 = new_mean1
        mean2 = new_mean2
        arr1 = np.zeros(0)
        arr2 = np.zeros(0)
    
    clusterAssignments = np.zeros(0)
    for i in range(np.shape(arr)[0]):
        clusterAssignments = np.append(clusterAssignments,arr[i][1]).astype(int)
    return clusterAssignments    



def removeIncomplete(id):
    id_int = id.astype(int)

    id_int.sort()
    #print(id_int)
    idComplete = np.empty(0)
    for x in id:
        #print(x)
        if np.count_nonzero(id_int == x.astype(int)) == 3:
            idComplete = np.append(idComplete,x)
    return idComplete


def bacteriaGrowth(n0, alpha, K, N):
    if n0>N:
        return 0
    n = (1+alpha * (1-(n0/K)))*n0
    tN = 1
    while True:
        tN = tN+1
        n = (1+alpha * (1-(n/K)))*n
        if n>N:
            break
    return tN

def fermentationRate(measuredRate, lowerBound, upperBound):
    arr = np.empty(0)
    for x in measuredRate:
        if np.less(x,upperBound) and np.greater(x,lowerBound):
            arr = np.append(arr,x)
    averageRate = np.mean(arr)
            
    return averageRate