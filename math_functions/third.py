import math


def test1(x, y1, y2, y3) -> float:
    return -y2 + math.sin(x * y3)


def test2(x, y1, y2, y3) -> float:
    return y1 ** 2


def test3(x, y1, y2, y3) -> float:
    return -y3 - y1


def exercise3_func1(x, y1, y2, y3) -> float:
    return math.sinh(x*y1+y2*y3)


def exercise3_func2(x, y1, y2, y3) -> float:
    return math.cosh(x*y1+y2*y3)


def exercise3_func3(x, y1, y2, y3) -> float:
    return math.sin(y1*y2+y3)


