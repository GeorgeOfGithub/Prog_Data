import math
import numpy as np


def pH2Category(pH):
    if pH<3.0:
        category = "Strongly acidic"
    elif pH<5.0:
        category = "Weakly acidic"
    elif pH<8.0:
        category = "Neutral"
    elif pH<11.0:
        category = "Weakly basic"
    elif pH<14.0:
        category = "Strongly basic"
    else:
        category = "pH out of range"
    return category


def gravitationalPull(x):
    g0 = 9.82
    R = 6.371*math.pow(10,6)
    if x < R:
        g=g0*(x/R)
    else:
        g=g0*(math.pow(R,2)/math.pow(x,2))
    return g


def acuteAngle(v1, v2):
    v = np.dot(v1,v2)
    angle = math.acos(v)
    if angle>(math.pi/2):
        theta = math.pi-angle
    else:
        theta = angle
    return theta

def computePassesGoalLine(point, directionVector):

    return score