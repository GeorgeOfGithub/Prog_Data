import math
import numpy as np

def thermoEquilibrium(N, r):
    t=1
    Nl = N
    Nr = 0.0
    for i in range(np.size(r)):
        plr = Nl/N

        if np.less_equal(r[i],plr) and Nl > 0:        
            Nl-=1
            Nr+=1
        else:
            Nl+=1
            Nr-=1
        if Nl == Nr:
            return t
        t+=1
    return 0

def circleAreaMC(xvals, yvals):
    r = 1
    N = np.size(xvals)

    n = np.zeros(0)
    for i in range(np.size(xvals)):
        if np.less_equal(np.hypot(xvals[i],yvals[i]), 1.0):
            n = np.append(n,1)
    A = 4 * np.size(n)/N
    return A

def convertTemperature(T, unitFrom, unitTo):
    if unitFrom == "Celsius":
        if unitTo == "Fahrenheit":
            T = 1.8 * T +32
        else:
            T = T + 273.15
    elif unitFrom == "Fahrenheit":
        if unitTo == "Celsius":
            T = (T-32)/(1.8)
        else:
            T = (T+459.67)/(1.8)
    else:
        if unitTo == "Celsius":
            T = T -273.15
        else:
            1.8*T-459.67
    return T