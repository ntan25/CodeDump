import random 
import math 


def calculatePi(dots):
    # xCoordinate = random.random(-1, 1)
    # yCoordinate = random.random(-1, 1)
    dotsIn = 0
    dotsOut = 0

    for i in range(dots): 
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        z = math.sqrt((x **2) + (y **2))
        if (z  <= 1): 
            dotsIn += 1
            dotsOut += 1
        else: 
            dotsOut += 1

    pi = 4 * dotsIn / dotsOut

    return (pi)


print(calculatePi(10000))
