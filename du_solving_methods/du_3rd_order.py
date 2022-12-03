import math
import help_part as hp


def euler(my_math_func1, my_math_func2, my_math_func3,
          x_0: float, x_k: float, y_0_1: float,
          y_0_2: float, y_0_3: float, h: float, step_round=None) -> list[tuple[float, float]]:
    res_list: list[tuple[float, float, float, float]] = []
    amount_points = int((x_k - x_0)/h)
    if step_round is None:  # not defined manually
        step_round = hp.find_step_round(h)
    x_i = x_0
    y_i1 = y_0_1
    y_i2 = y_0_2
    y_i3 = y_0_3
    res_list.append((round(x_i, step_round),
                    round(y_i1, step_round),
                    round(y_i2, step_round),
                    round(y_i3, step_round)))
    for i in range(amount_points):
        x_i += h
        y_i1 += h*my_math_func1(x_i, y_i1, y_i2, y_i3)
        y_i2 += h*my_math_func2(x_i, y_i1, y_i2, y_i3)
        y_i3 += h*my_math_func3(x_i, y_i1, y_i2, y_i3)
        res_list.append((round(x_i, step_round),
                        round(y_i1, step_round),
                        round(y_i2, step_round),
                        round(y_i3, step_round)))
    return res_list


def runge_Kutta4(my_math_func1, my_math_func2, my_math_func3,
                 x_0: float, x_k: float, y_0_1: float,
                 y_0_2: float, y_0_3: float, h: float,
                 ) -> list[tuple[float, float]]:
    if step_round is None:  # not defined manually
        step_round = hp.find_step_round(h)
    res_list: list[tuple[float, float, float, float]] = []
    amount_points = int((x_k - x_0)/h)
    x_i = x_0
    y_i1 = y_0_1
    y_i2 = y_0_2
    y_i3 = y_0_3
    res_list.append((round(x_i, step_round),
                    round(y_i1, step_round),
                    round(y_i2, step_round),
                    round(y_i3, step_round)))

    for i in range(amount_points):
        x_i += h
        k1_1 = h*my_math_func1(x_i, y_i1, y_i2, y_i3)
        k1_2 = h*my_math_func2(x_i, y_i1, y_i2, y_i3)
        k1_3 = h*my_math_func3(x_i, y_i1, y_i2, y_i3)

        k2_1 = h * my_math_func1(x_i+h/2, y_i1+k1_1/2,
                                 y_i2+k1_1/2, y_i3+k1_1/2)
        k2_2 = h * my_math_func2(x_i+h/2, y_i1+k1_2/2,
                                 y_i2+k1_2/2, y_i3+k1_2/2)
        k2_3 = h * my_math_func3(x_i+h/2, y_i1+k1_3/2,
                                 y_i2+k1_3/2, y_i3+k1_3/2)

        k3_1 = h * my_math_func1(x_i+h/2, y_i1+k2_1/2,
                                 y_i2+k2_1/2, y_i3+k2_1/2)
        k3_2 = h * my_math_func2(x_i+h/2, y_i1+k2_2/2,
                                 y_i2+k2_2/2, y_i3+k2_2/2)
        k3_3 = h * my_math_func3(x_i+h/2, y_i1+k2_3/2,
                                 y_i2+k2_3/2, y_i3+k2_3/2)

        k4_1 = h * my_math_func1(x_i+h, y_i1+k3_1, y_i2+k3_1/2, y_i3+k3_1/2)
        k4_2 = h * my_math_func2(x_i+h, y_i1+k3_2, y_i2+k3_2/2, y_i3+k3_2/2)
        k4_3 = h * my_math_func3(x_i+h, y_i1+k3_3, y_i2+k3_3/2, y_i3+k3_3/2)

        y_i1 += (k1_1+2*k2_1+2*k3_1+k4_1)/6
        y_i2 += (k1_2+2*k2_2+2*k3_2+k4_2)/6
        y_i3 += (k1_3+2*k2_3+2*k3_3+k4_3)/6
        res_list.append((round(x_i, step_round),
                        round(y_i1, step_round),
                        round(y_i2, step_round),
                        round(y_i3, step_round)))
    return res_list


def runge_kutta5(my_math_func1, my_math_func2, my_math_func3,
                 x_0: float, x_k: float, y_0_1: float,
                 y_0_2: float, y_0_3: float, h: float, step_round=None) -> list[tuple[float, float]]:
    res_list: list[tuple[float, float, float, float]] = []
    amount_points = int((x_k - x_0)/h)
    if step_round is None:  # not defined manually
        step_round = hp.find_step_round(h)
    x_i = x_0
    y_i1 = y_0_1
    y_i2 = y_0_2
    y_i3 = y_0_3
    res_list.append((round(x_i, step_round),
                    round(y_i1, step_round),
                    round(y_i2, step_round),
                    round(y_i3, step_round)))
    for i in range(amount_points):
        x_i += h
        k0_1 = h*my_math_func1(x_i, y_i1, y_i2, y_i3)
        k0_2 = h*my_math_func2(x_i, y_i1, y_i2, y_i3)
        k0_3 = h*my_math_func3(x_i, y_i1, y_i2, y_i3)

        k1_1 = h * my_math_func1(x_i+h/3, y_i1+k0_1/3,
                                 y_i2+k0_1/3, y_i3+k0_1/3)
        k1_2 = h * my_math_func2(x_i+h/3, y_i1+k0_2/3,
                                 y_i2+k0_2/3, y_i3+k0_2/3)
        k1_3 = h * my_math_func3(x_i+h/3, y_i1+k0_3/3,
                                 y_i2+k0_2/3, y_i3+k0_3/3)

        k2_1 = h * my_math_func1(x_i+h/3, y_i1+k0_1/6 +
                                 k1_1/6, y_i2+k0_1/6+k1_1/6, y_i3+k0_1/6+k1_1/6)
        k2_1 = h * my_math_func1(x_i+h/3, y_i1+k0_2/6 +
                                 k1_2/6, y_i2+k0_2/6+k1_2/6, y_i3+k0_2/6+k1_2/6)
        # Todo: complete runge_Kutta4
        k3 = h * \
            my_math_func(x_i+h/2, y_i+k0/8+3*k2/8)
        k4 = h * \
            my_math_func(x_i+h,
                         y_i+k0/2-3*k2/2+2*k3)
        y_i += (k0+4*k3+k4)/6
        res_list.append((round(x_i, step_round),
                        round(y_i1, step_round),
                        round(y_i2, step_round),
                        round(y_i3, step_round)))
    return res_list


def test1(x, y1, y2, y3) -> float:
    return -y2 + math.sin(x*y3)


def test2(x, y1, y2, y3) -> float:
    return y1**2


def test3(x, y1, y2, y3) -> float:
    return -y3-y1


if __name__ == '__main__':
    res_lt1 = runge_Kutta4(test1, test2, test3, 0, 2, 1, 0, 1, 10**-4)
    res_lt2 = euler(test1, test2, test3, 0, 2, 1, 0, 1, 10**-4)
    hp.pretty_print_el4(res_lt1)
    print("\n\n")
    hp.pretty_print_el4(res_lt2)
