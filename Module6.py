import math
import numpy as np
import pandas as pd

def letterFrequency(filename):
    filein = open(filename, "r")
    lines = filein.readlines()
    txt = "".join(lines)
    txt = txt.lower()
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters = np.array(letters)
    freq = np.zeros(0)
    noletters = 0
    for i in range(np.size(letters)):
        count = np.char.count(txt, letters[i])
        noletters += count 
        freq = np.append(freq,count)

    
    for i in range(np.size(freq)):
        freq[i] = np.divide(freq[i],noletters) * 100
    
    return freq

def movingAvg(y):
    y2= 2*y
    y3=3*y
    row1 = np.pad(y,((0,2)), mode='constant')[2:]
    row2 = np.pad(y2,((0,1)), mode='constant')[1:]
    row3 = np.pad(y3,((0,0)), mode='constant')[:]
    row4 = np.pad(y2,((1,0)), mode='constant')[:-1]
    row5 = np.pad(y,((2,0)), mode='constant')[:-2]
    A = np.array([row1,row2,row3,row4,row5])
    ysmooth = np.zeros(0)
    for i in range(np.size(A[0,:])):
        ysmooth = np.append(np.sum(A[:,i])/9,ysmooth)
    ysmooth = np.flip(ysmooth)
    return ysmooth


def computeItemCost(resourceItemMatrix, resourceCost):
    A = resourceItemMatrix
    B = resourceCost
    A = A.T
    itemCost = np.dot(A,B)

    return itemCost

def computeLanguageError(freq):
    letters = pd.read_csv("letter_frequencies.csv")
    print(letters)
    E = np.zeros(0)

    for j in range(15):
        arr = np.array(letters.iloc[:,j+1])
        sum = 0
        for i in range(26):
            
            sum += np.power(freq[i]- arr[i],2)
            

        E =np.append(sum,E)
    E = np.flip(E)
        
        
    return E

print(computeLanguageError("nice"))