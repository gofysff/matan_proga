import math


def exercise4_func1(x, y1, y2, y3) -> float:
    return y2


def exercise4_func2(x, y1, y2, y3) -> float:
    return y3


def exercise4_func3(x, y1, y2, y3) -> float:
    try:
        return math.cos(x / (x + 2)) - y1 * math.atan(x * x + 4) - (math.e ** x) * y2 - 2 * y3
    except ZeroDivisionError:
        return math.cos(x / (x + 2+10**-6)) - y1 * math.atan(x * x + 4) - (math.e ** x) * y2 - 2 * y3