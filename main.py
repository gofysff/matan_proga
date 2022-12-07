import math

import organised_exercises as ready_ex
import math_functions as mf


def done_first_number():
    # global x_0, x_k, eps
    """first exercise"""
    math_func_1exercise = mf.my_func1_exersise1
    x_0 = 1
    x_k = 6
    y_0 = -0.5
    eps = 10 ** -4
    ready_ex.first_exercise(x_0, x_k, y_0, eps, math_func_1exercise, step_showing=0.5)


def done_second_number():
    # global x_0, x_k, y_0_0, y_0_1, eps
    """second exercise"""
    math_func1_2exercise = mf.my_func1_exersise2
    math_func2_2exercise = mf.my_func2_exersise2
    x_0 = 2
    x_k = 7
    y_0_0 = 0.2
    y_0_1 = -3
    eps = 10 ** -4
    ready_ex.second_exercise(x_0, x_k, y_0_0, y_0_1, eps, math_func1_2exercise, math_func2_2exercise, step_showing=0.5)


def done_third_number():
    # global x_0, x_k, y_0_0, y_0_1, y_0_2, step_showing, eps
    """third exercise"""
    math_func1_3exercise = mf.exercise3_func1
    math_func2_3exercise = mf.exercise3_func2
    math_func3_3exercise = mf.exercise3_func3
    x_0 = 0.75
    x_k = 2
    y_0_0 = 0.3
    y_0_1 = -1
    y_0_2 = 0.4
    step_showing = 0.125
    eps = 10 ** -6
    ready_ex.third_exercise(x_0, x_k, y_0_0, y_0_1, y_0_2, eps, math_func1_3exercise, math_func2_3exercise,
                            math_func3_3exercise, step_showing)


def done_fourth_number():
    # global x_0, x_k, y_0_0, y_0_1, y_0_2, step_showing, eps
    """fourth exercise"""
    math_func1_4exercise = mf.exercise4_func1
    math_func2_4exercise = mf.exercise4_func2
    math_func3_4exercise = mf.exercise4_func3
    x_0 = round(- math.pi, 6)
    x_k = round(math.pi, 6)
    y_0_0 = 0
    y_0_1 = 1
    y_0_2 = -2
    step_showing = round(math.pi * 2 / 10, 6)
    eps = 10 ** -6
    ready_ex.fourth_exercise(x_0, x_k, y_0_0, y_0_1, y_0_2, eps, math_func1_4exercise, math_func2_4exercise,
                             math_func3_4exercise, step_showing)


def done_zashita():
    # global x_0, x_k, eps
    def func_for_zachity(x, y) -> float:
        return x ** 2 - 2 * y

    math_func_zachita = func_for_zachity
    x_0 = 0
    x_k = 1
    y_0 = 1
    eps = 10 ** -5
    ready_ex.first_exercise(x_0, x_k, y_0, eps, math_func_zachita, step_showing=0.1)


if __name__ == "__main__":
    """for clarity, we display all the variables here, which are given by condition in the task"""
    """ uncomment what u want to display"""
    # done_first_number()
    #
    # done_second_number()
    #
    # done_third_number()
    #
    # done_fourth_number()

    # done_zashita()
