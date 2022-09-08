import math
import numpy as np

def computeProjection(a):  
    b = np.ones(np.size(a))
    t = np.dot(a,b)
    a1 = np.power(a,2)
    n = np.sum(a1)
    projection = (t/n)*a
    return projection

def boxArea(boxCorners, area):
    A1 = (boxCorners[1]-boxCorners[0])*(boxCorners[5]-boxCorners[4])
    A2 = (boxCorners[3]-boxCorners[2])*(boxCorners[7]-boxCorners[6])
    intersection = max([0,(min(boxCorners[1],boxCorners[3])-max(boxCorners[0],boxCorners[2]))])*max([0,(min(boxCorners[5],boxCorners[7])-max(boxCorners[4],boxCorners[6]))])
    if area == "Box1":
        A=A1
    elif area == "Box2":
        A=A2
    elif area == "Intersection":
        A=intersection
    elif area == "Union":
        A=A1+A2-intersection
    return A

def evaluateTaylor(x):
    y = (x-1)-0.5*math.pow((x-1),2)+(1/3)*math.pow((x-1),3)
    return y



def fillSudokuRow(sudokuRow):
    for n in sudokuRow:
        if sudokuRow[n-1] == 0:
            sudokuRow[n-1] = 45-np.sum(sudokuRow)           
    return sudokuRow
