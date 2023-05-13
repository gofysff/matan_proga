import numpy as np
from math import *

def result(x, X, Y):
    n = X.shape[0]
    L = 0
    save = [] # для сохранения знаминателей слогаемых лагранжа
    for i in range(n):
        li = 1.0
        tmp = 1.0
        for j in range(n):
            if(j!=i):
                li *= (x-X[j])/(X[i]-X[j])
                tmp /=(X[i]-X[j])
        save.append(tmp)
        L += Y[i]*li
    return L
