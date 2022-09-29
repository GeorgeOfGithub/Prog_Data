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
