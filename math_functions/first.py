import math


def my_func1_exersise1(x: float, y: float) -> float:
    return x*math.cos((x**2 * y)/(x-y))


def test_func1(x: float, y: float) -> float:
    return x**2*math.sin(x)-3*y
