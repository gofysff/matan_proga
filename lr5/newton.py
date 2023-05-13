import numpy as np
from math import *


def result(x, X, Y):
    n = Y.shape[0]+1  # хз, н0 нужно +1 сделать
    P = 0.0  # Y[0]  # а тут y0 убрать
    for k in range(1, n):
        f = 0.0
        for i in range(k):
            g = 1.0
            for j in range(k):
                if j != i:
                    g *= (X[i]-X[j])
            f += Y[i]/g
        ok = 1.0
        for i in range(k-1):
            ok *= (x-X[i])
        P += f*ok
    return P
