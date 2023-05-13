import numpy as np
import matplotlib.pyplot as plt
from math import *
import random

import lagranj
import newton
import spline3
import spline2
import aprox1
import aprox2


plt.grid(True)
# Вариант 28
# -10

# a = 7.0
# b = 5.0
# k = 1.
# c = 1.
# d = 16.
# m = 6
# n = 3

a = 8.0
b = 3.0
k = 3.
c = 1.
d = 24.
m = 8
n = 5

l = (d-c)/(m*n)
Y2 = np.array([(log(i*l+c))**(a/b) * sin(k*i*l+c) for i in range(m*n+1)])
X2 = np.array([i*l+c for i in range(m*n+1)])

# X1 = np.array([0.345, 0.761, 1.257, 2.109, 2.943])
# Y1 = np.array([-1.221, -0.525, 2.314, 5.106, 9.818])

X1 = np.array([0.452, 0.967, 2.255, 4.013, 5.432])
Y1 = np.array([1.252, 2.015, 4.342, 5.752, 6.911])


# X3 = np.array([0.248, 0.584, 0.921, 1.257, 1.593, 1.930, 2.266, 2.603, 2.939])
# Y3 = np.array([-3.642, 0.797, 0.844, 0.829, 0.647, 0.678, 0.633, 0.549, 0.328])

X3 = np.array([0.105, 0.449, 0.794, 1.138, 1.482, 1.826, 2.171, 2.515, 2.859])
Y3 = np.array([-4.215, -3.889, -3.942, -4.595, -
              5.765, -7.484, -10.771, -15.904, -22.938])

# X3 = np.array([0.034, 0.394, 0.75, 1.114, 1.474, 1.833, 2.193, 2.553, 2.913])
# Y3 = np.array([2.156, 2.988, 3.377, 3.708, 3.802, 3.9, 4.067, 4.129, 4.171])


def zadan1():
    plt.title("задание 1-2")

    points1, = plt.plot(X1, Y1, 'b+')

    # начало, конец графика(по x) и количестов точек
    start = X1[0]
    finish = X1[-1]
    dot_count = 400
    step = (finish-start)/(dot_count-1)

    Ly = np.array([lagranj.result(i*step+start, X1, Y1)
                  for i in range(0, dot_count)])
    Lx = np.array([i*step+start for i in range(0, dot_count)])
    plot1, = plt.plot(Lx, Ly, linestyle='solid')

    Py = np.array([newton.result(i*step+start, X1, Y1)
                  for i in range(0, dot_count)])
    Px = np.array([i*step+start for i in range(0, dot_count)])
    plot2, = plt.plot(Px, Py, linestyle='solid')

    # очищение графика от 1 и 2 задания
    plt.waitforbuttonpress()
    points1.remove()
    plot1.remove()
    plot2.remove()


def zadan3():
    plt.title("задание 3")
    points2 = plt.plot(X2, Y2, 'b+')

    start = c
    finish = d
    dot_count = 100
    step = (finish-start)/(dot_count-1)

    gY = np.array([(log(i*step+c))**(a/b) * sin(k*i*step+c)
                  for i in range(dot_count)])
    gX = np.array([i*step+start for i in range(dot_count)])
    func2, = plt.plot(gX, gY, linestyle='solid')

    # тут функцию на отрезочки по n штук режим
    start = c
    finish = d
    dot_count = 10
    step = (finish-start)/(dot_count-1)

    plots3 = []
    for ok in range(0, n*m, n):
        st = c+ok*l
        h = (c+(ok+n)*l-st)/(dot_count-1)

        Ly = np.array([lagranj.result(i*h+st, X2[ok:ok+n+1], Y2[ok:ok+n+1])
                      for i in range(dot_count)])
        Lx = np.array([i*h+st for i in range(dot_count)])
        current_plot, = plt.plot(Lx, Ly, linestyle='solid')
        plots3.append(current_plot)

    plt.waitforbuttonpress()
    for i in range(len(plots3)):
        plots3[i].remove()
    func2.remove()


def zadan4():
    plt.title("задание 4")
    # используется X Y из предеыдущего задания
    start = c
    finish = d
    dot_count = 100
    step = (finish-start)/(dot_count-1)

    gY = np.array([(log(i*step+c))**(a/b) * sin(k*i*step+c)
                  for i in range(dot_count)])
    gX = np.array([i*step+start for i in range(dot_count)])
    func2, = plt.plot(gX, gY, linestyle='solid')

    points2, = plt.plot(X2, Y2, 'b+')

    start = c
    finish = d
    dot_count = 30
    step = (finish-start)/(dot_count-1)

    Sy = np.array([spline2.result(i*step+start, X2, Y2)
                  for i in range(dot_count)])
    Sx = np.array([i*step+start for i in range(dot_count)])
    plot4, = plt.plot(Sx, Sy, linestyle='solid')

    plt.waitforbuttonpress()
    plot4.remove()
    func2.remove()
    points2.remove()


def zadan5():
    plt.title("задание 5")
    # используется X Y из предеыдущего задания
    start = c
    finish = d
    dot_count = 100
    step = (finish-start)/(dot_count-1)

    gY = np.array([(log(i*step+c))**(a/b) * sin(k*i*step+c)
                  for i in range(dot_count)])
    gX = np.array([i*step+start for i in range(dot_count)])
    func2, = plt.plot(gX, gY, linestyle='solid')

    points2, = plt.plot(X2, Y2, 'b+')

    start = c
    finish = d
    dot_count = 50
    step = (finish-start)/(dot_count-1)
    Sy = np.array([spline3.result(i*step+start, X2, Y2)
                  for i in range(dot_count)])
    Sx = np.array([i*step+start for i in range(dot_count)])
    plot5, = plt.plot(Sx, Sy, linestyle='solid')


def zadan6():
    plt.title("задание 6")

    points1, = plt.plot(X3, Y3, 'b+')

    A1y = np.array([aprox1.result(i*(X3[-1]-X3[0])+X3[0], X3, Y3)
                   for i in range(0, 2)])
    A1x = np.array([i*(X3[-1]-X3[0])+X3[0] for i in range(0, 2)])
    plot1, = plt.plot(A1x, A1y, linestyle='solid')

    start = min(X3)
    finish = max(X3)
    dot_count = 30
    step = (finish-start)/(dot_count-1)
    A2x = np.array([aprox2.result(i*step+start, X3, Y3)
                   for i in range(dot_count)])
    A2y = np.array([i*step+start for i in range(dot_count)])
    plot2, = plt.plot(A2x, A2y, linestyle='solid')

    # очищение графика от 1 и 2 задания
    plt.waitforbuttonpress()
    # points1.remove()
    # plot1.remove()
    # plot2.remove()


# zadan1()
# zadan3()
zadan4()
# zadan5()
# zadan6()

plt.show()
