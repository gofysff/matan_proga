import math


def find_step_round(step_integrate: float) -> int:
    '''step integrate is eps'''
    return int(math.log10(1/step_integrate))


def pretty_print_result2el(res_lt: list[tuple[float, float]], step_print):
    '''one dimensional list with tuple of 2 floats'''
    for val in res_lt:
        if val[0] % step_print == 0:
            print(f'x is {val[0]:5}\ty is {val[1]:7}')


def template_method(method, my_math_func, x_intial: float, x_end: float, y_intial: float,
                    step_integrate: float) -> list[tuple[float, float]]:
    """
    x_intial is the x0
    x_end is the x_k
    y_intial is the y0
    step_integrate is the eps or 'h'
    amount_points_integrate is the n"""
    step_round = find_step_round(step_integrate)
    res_list: list[tuple[float, float]] = []
    amount_points_integrate = int((x_end - x_intial)/step_integrate)
    x_current = x_intial
    y_current = y_intial
    res_list.append((round(x_current, step_round),
                    round(y_current, step_round)))
    return method(my_math_func, step_integrate, step_round, res_list,
                  amount_points_integrate, x_current, y_current)


def Euler(my_math_func, x_intial: float, x_end: float, y_intial: float,
          step_integrate: float) -> list[tuple[float, float]]:
    """
    x_intial is the x0
    x_end is the x_k
    y_intial is the y0
    step_integrate is the eps
    amount_points_integrate is the n"""
    step_round = find_step_round(step_integrate)
    res_list: list[tuple[float, float]] = []
    amount_points_integrate = int((x_end - x_intial)/step_integrate)
    x_current = x_intial
    y_current = y_intial
    res_list.append((round(x_current, step_round),
                    round(y_current, step_round)))

    for i in range(amount_points_integrate):
        x_current += step_integrate
        y_current += step_integrate*my_math_func(x_current, y_current)
        res_list.append((round(x_current, step_round),
                        round(y_current, step_round)))
    return res_list


def Runge_Kutta4(my_math_func, x_intial: float, x_end: float, y_intial: float,
                 step_integrate: float) -> list[tuple[float, float]]:
    """
    x_intial is the x0
    x_end is the x_k
    y_intial is the y0
    step_integrate is the eps or 'h'
    amount_points_integrate is the n"""
    step_round = find_step_round(step_integrate)
    res_list: list[tuple[float, float]] = []
    amount_points_integrate = int((x_end - x_intial)/step_integrate)
    x_current = x_intial
    y_current = y_intial
    res_list.append((round(x_current, step_round),
                    round(y_current, step_round)))

    return runge_kutta4(my_math_func, step_integrate, step_round, res_list, amount_points_integrate, x_current, y_current)


def runge_kutta4(my_math_func, step_integrate, step_round, res_list, amount_points_integrate, x_current, y_current):
    for i in range(amount_points_integrate):
        x_current += step_integrate
        k1 = step_integrate*my_math_func(x_current, y_current)
        k2 = step_integrate * \
            my_math_func(x_current+step_integrate/2, y_current+k1/2)
        k3 = step_integrate * \
            my_math_func(x_current+step_integrate/2, y_current+k2/2)
        k4 = step_integrate * \
            my_math_func(x_current+step_integrate, y_current+k3)
        y_current += (k1+2*k2+2*k3+k4)/6
        res_list.append((round(x_current, step_round),
                        round(y_current, step_round)))
    return res_list

# def


def my_func1(x: float, y: float) -> float:
    return x*math.cos((x**2 * y)/(x-y))


def my_func2(x: float, y: float) -> float:
    return x**2*math.sin(x)-3*y


if __name__ == "__main__":
    # x_0 = 0
    # x_k = 20
    # y_0 = 40
    # eps = 0.0001
    # res1 = Euler(my_func2, x_0, x_k, y_0, eps)

    x_0 = 1
    x_k = 6
    y_0 = -0.5
    eps = 0.0001
    # print(len(res))
    # # # print(res)
    # # for val in res:
    # #     if val[0] % 2 == 0:
    # #         print(val)
    # print(find_step_round(0.0001))
    res2 = Runge_Kutta4(my_func2, x_0, x_k, y_0, eps)
    pretty_print_result2el(res1, 2)
    print("\n\n")
    pretty_print_result2el(res2, 2)
