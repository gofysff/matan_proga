import numpy as np
from math import *


def result(x, X,Y):
    n = X.shape[0]
    
    Bt = [0.]
    for i in range(1,n):
        Bt.append(2.*(Y[i]-Y[i-1])/(X[i]-X[i-1]) - Bt[i-1])
    B = np.array(Bt)
    
    C = np.array([ (B[i+1] - B[i])/2./(X[i+1]-X[i])  for i in range(n-1) ])
    
    #print("B:", B)
    #print("C:", C)
    
    i = int(x//((X[-1]-X[0])/(n-1))-1)
    if(i>(n-2)): i=n-2
    return Y[i] + B[i]*(x-X[i]) + C[i]*(x-X[i])**2
