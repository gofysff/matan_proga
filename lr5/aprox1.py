import numpy as np
from math import *


def result(x, X,Y):
    n = X.shape[0]
    
    Sxy = Sx = Sy = Sx2 = 0
    for i in range(n):
        Sxy += X[i]*Y[i]
        Sx += X[i]
        Sy += Y[i]
        Sx2 += X[i]**2
        
    A = (n*Sxy - Sx*Sy)/(n*Sx2 - Sx**2)
    B = (Sy - A*Sx)/n

    return x*A + B
