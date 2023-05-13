import numpy as np
import scipy as sc
from math import *


def result(x, X,Y):
    n = X.shape[0]
    
    # для решения прогонкой
    C_tmp = []
    # а здорова ты это придумал я даже сначала не понял. молодец
	# библиотека scipy для решения метода прогонки использует н обычную матрицу, а просто диагональные элементы.
	# тобежь:
	# 1 2 0 0 0    
	# 2 1 2 0 0    [0,2,2,2,2]
	# 0 2 1 2 0  = [1,1,1,1,1]
	# 0 0 2 1 2	   [2,2,2,2,0]
	# 0 0 0 2 1
    C_tmp.append([1.]*(n-2))
    C_tmp.append([4.]*(n-2))
    C_tmp.append([1.]*(n-2))
    C_tmp[0][0] = 0
    C_tmp[-1][-1] = 0
    C_tmp = np.array(C_tmp)
    Bc = np.array([3./(X[i+1]-X[i])**2 * (Y[i]-Y[i+1]*2.+Y[i+2]) for i in range(n-2)])
    # решаем слау методом прогонки
    C = sc.linalg.solve_banded((1,1),C_tmp, Bc)
    C = np.insert(C,0,0.) # добавляем в начало 0
    
    D = [(C[i+1]-C[i])/(3.*(X[i+1]-X[i])) for i in range(n-2)]
    D.append(-C[n-2]/(3.*(X[n-2]-X[n-1]))) #chek kek
    D = np.array(D)
    B = np.array([(Y[i] - Y[i-1])/(X[i]-X[i-1]) - C[i-1]*(X[i]-X[i-1]) - D[i-1]*(X[i]-X[i-1])**2 for i in range(1,n)])
    
    #print("B:", B)
    #print("C:", C)
    #print("D:", D)


    i = int(x//((X[-1]-X[0])/(n-1))-1)
    if(i>(n-2)): i=n-2
    return (Y[i]+B[i]*(x-X[i]) + C[i]*(x-X[i])**2 + D[i]*(x-X[i])**3) 
