import help_part as hp


def euler(my_math_func1, my_math_func2,
          x_0: float, x_k: float, y_0_1: float,
          y_0_2: float, h: float, step_round=None) -> list[tuple[float, float, float]]:
    res_list: list[tuple[float, float, float]] = []
    amount_points = int((x_k - x_0) / h)
    if step_round is None:  # not defined manually
        step_round = hp.find_step_round(h)
    x_i = x_0
    y_i1 = y_0_1
    y_i2 = y_0_2
    res_list.append((round(x_i, step_round),
                     round(y_i1, step_round),
                     round(y_i2, step_round)))
    for i in range(amount_points):
        x_i += h
        y_i1 += h * my_math_func1(x_i, y_i1, y_i2)
        y_i2 += h * my_math_func2(x_i, y_i1, y_i2)
        res_list.append((round(x_i, step_round),
                         round(y_i1, step_round),
                         round(y_i2, step_round)))
    return res_list


def runge_kutta4(my_math_func1, my_math_func2,
                 x_0: float, x_k: float, y_0_1: float,
                 y_0_2: float, h: float, step_round=None) -> list[tuple[float, float, float]]:
    res_list: list[tuple[float, float, float]] = []
    amount_points = int((x_k - x_0) / h)
    if step_round is None:  # not defined manually
        step_round = hp.find_step_round(h)
    x_i = x_0
    y_i1 = y_0_1
    y_i2 = y_0_2
    res_list.append((round(x_i, step_round),
                     round(y_i1, step_round),
                     round(y_i2, step_round)))

    for i in range(amount_points):
        x_i += h
        k1_1 = h * my_math_func1(x_i, y_i1, y_i2)
        k1_2 = h * my_math_func2(x_i, y_i1, y_i2)

        k2_1 = h * my_math_func1(x_i + h / 2, y_i1 + k1_1 / 2,
                                 y_i2 + k1_1 / 2)
        k2_2 = h * my_math_func2(x_i + h / 2, y_i1 + k1_2 / 2,
                                 y_i2 + k1_2 / 2)

        k3_1 = h * my_math_func1(x_i + h / 2, y_i1 + k2_1 / 2,
                                 y_i2 + k2_1 / 2)
        k3_2 = h * my_math_func2(x_i + h / 2, y_i1 + k2_2 / 2,
                                 y_i2 + k2_2 / 2)

        k4_1 = h * my_math_func1(x_i + h, y_i1 + k3_1, y_i2 + k3_1 / 2)
        k4_2 = h * my_math_func2(x_i + h, y_i1 + k3_2, y_i2 + k3_2 / 2)

        y_i1 += (k1_1 + 2 * k2_1 + 2 * k3_1 + k4_1) / 6
        y_i2 += (k1_2 + 2 * k2_2 + 2 * k3_2 + k4_2) / 6

        res_list.append((round(x_i, step_round),
                         round(y_i1, step_round),
                         round(y_i2, step_round)))
    return res_list


def runge_kutta5(my_math_func1, my_math_func2,
                 x_0: float, x_k: float, y_0_1: float,
                 y_0_2: float, h: float, step_round=None) -> list[tuple[float, float, float]]:
    res_list: list[tuple[float, float, float]] = []
    amount_points = int((x_k - x_0) / h)
    if step_round is None:  # not defined manually
        step_round = hp.find_step_round(h)
    x_i = x_0
    y_i1 = y_0_1
    y_i2 = y_0_2
    res_list.append((round(x_i, step_round),
                     round(y_i1, step_round),
                     round(y_i2, step_round)))

    for i in range(amount_points):
        x_i += h
        k0_1 = h * my_math_func1(x_i, y_i1, y_i2)
        k0_2 = h * my_math_func2(x_i, y_i1, y_i2)

        k1_1 = h * my_math_func1(x_i + h / 3, y_i1 + k0_1 / 3, y_i2 + k0_1 / 3)
        k1_2 = h * my_math_func2(x_i + h / 3, y_i1 + k0_2 / 3, y_i2 + k0_2 / 3)

        k2_1 = h * my_math_func1(x_i + h / 3, y_i1 + k0_1 / 6 +
                                 k1_1 / 6, y_i2 + k0_1 / 6 + k1_1 / 6)
        k2_2 = h * my_math_func2(x_i + h / 3, y_i1 + k0_2 / 6 +
                                 k1_2 / 6, y_i2 + k0_2 / 6 + k1_2 / 6)

        k3_1 = h * my_math_func1(x_i + h / 2, y_i1 + k0_1 / 8 + 3 * k2_1 / 8, y_i2 + k0_1 / 8 + 3 * k2_1 / 8)
        k3_2 = h * my_math_func2(x_i + h / 2, y_i1 + k0_2 / 8 + 3 * k2_2 / 8, y_i2 + k0_2 / 8 + 3 * k2_1 / 8)
        k4_1 = h * my_math_func1(x_i + h,
                                 y_i1 + k0_1 / 2 - 3 * k2_1 / 2 + 2 * k3_1, y_i2 + k0_1 / 2 - 3 * k2_1 / 2 + 2 * k3_1)
        k4_2 = h * my_math_func2(x_i + h,
                                 y_i1 + k0_2 / 2 - 3 * k2_2 / 2 + 2 * k3_2, y_i2 + k0_2 / 2 - 3 * k2_2 / 2 + 2 * k3_2)

        y_i1 += (k0_1 + 4 * k3_1 + k4_1) / 6
        y_i2 += (k0_2 + 4 * k3_2 + k4_2) / 6

        res_list.append((round(x_i, step_round),
                         round(y_i1, step_round),
                         round(y_i2, step_round)))
    return res_list


def adams_bashfort(my_math_func1, my_math_func2,
                 x_0: float, x_k: float, y_0_1: float,
                 y_0_2: float, h: float, step_round=None) -> list[tuple[float, float, float]]:
    res_list: list[tuple[float, float, float]] = []
    amount_points = int((x_k - x_0) / h)
    if step_round is None:  # not defined manually
        step_round = hp.find_step_round(h)
    x_i = x_0
    y_i1 = y_0_1
    y_i2 = y_0_2
    res_list.append((round(x_i, step_round),
                     round(y_i1, step_round),
                     round(y_i2, step_round)))

    for i in range(3):
        x_i += h
        k1_1 = h * my_math_func1(x_i, y_i1, y_i2)
        k1_2 = h * my_math_func2(x_i, y_i1, y_i2)

        k2_1 = h * my_math_func1(x_i + h / 2, y_i1 + k1_1 / 2, y_i2 + k1_1 / 2)
        k2_2 = h * my_math_func2(x_i + h / 2, y_i1 + k1_2 / 2, y_i2 + k1_2 / 2)

        k3_1 = h * my_math_func1(x_i + h / 2, y_i1 + k2_1 / 2, y_i2 + k2_1 / 2)
        k3_2 = h * my_math_func2(x_i + h / 2, y_i1 + k2_2 / 2, y_i2 + k2_2 / 2)

        k4_1 = h * my_math_func1(x_i + h, y_i1 + k3_1, y_i2 + k3_1)
        k4_2 = h * my_math_func2(x_i + h, y_i1 + k3_2, y_i2 + k3_2)

        y_i1 += (k1_1 + 2 * k2_1 + 2 * k3_1 + k4_1) / 6
        y_i2 += (k1_2 + 2 * k2_2 + 2 * k3_2 + k4_2) / 6
        res_list.append((round(x_i, step_round),
                         round(y_i1, step_round),
                         round(y_i2, step_round)))

    for i in range(3, amount_points):
        x_i += h
        k1_1 = h * my_math_func1(x_i, y_i1, y_i2)
        k1_2 = h * my_math_func2(x_i, y_i1, y_i2)

        k2_1 = h * my_math_func1(res_list[-1][0], res_list[-1][1], res_list[-1][2])
        k2_2 = h * my_math_func2(res_list[-1][0], res_list[-1][1], res_list[-1][2])

        k3_1 = h * my_math_func1(res_list[-2][0], res_list[-2][1], res_list[-2][2])
        k3_2 = h * my_math_func2(res_list[-2][0], res_list[-2][1], res_list[-2][2])

        k4_1 = h * my_math_func1(res_list[-3][0], res_list[-3][1], res_list[-3][2])
        k4_2 = h * my_math_func2(res_list[-3][0], res_list[-3][1], res_list[-3][2])

        y_i1 += (55 * k1_1 - 59 * k2_1 + 37 * k3_1 - 9 * k4_1) / 24
        y_i2 += (55 * k1_2 - 59 * k2_2 + 37 * k3_2 - 9 * k4_2) / 24
        res_list.append((round(x_i, step_round),
                         round(y_i1, step_round),
                         round(y_i2, step_round)))
    return res_list


def adams_meulton(my_math_func1, my_math_func2,
                 x_0: float, x_k: float, y_0_1: float,
                 y_0_2: float, h: float, step_round=None, res_adams_bashfort=None) -> list[tuple[float, float, float]]:
    if res_adams_bashfort is None:  # adams_meulton based on adams_bashfort
        res_list = adams_bashfort(my_math_func1, my_math_func2,x_0, x_k, y_0_1,
                                  y_0_2, h, step_round)
    else:
        res_list = res_adams_bashfort

    if step_round is None:  # not defined manually
        step_round = hp.find_step_round(h)
    amount_points = int((x_k - x_0) / h)
    y_list = [list(el[1:]) for el in res_list]  # let's make copy of all list y1, y2
    # res_list will contain x, y1, y2, y3
    res_list = [list(pair) for pair in res_list]  # type: ignore
    # make res_list changeable
    for i in range(2, amount_points - 1):
        for m in range(10):
            k1_1 = h * my_math_func1(res_list[i + 1][0], y_list[i + 1][0], y_list[i + 1][1])
            k1_2 = h * my_math_func2(res_list[i + 1][0], y_list[i + 1][0], y_list[i + 1][1])

            k2_1 = h * my_math_func1(res_list[i][0], *y_list[i])
            k2_2 = h * my_math_func2(res_list[i][0], *y_list[i])

            k3_1 = h * my_math_func1(res_list[i - 1][0], *y_list[i - 1])
            k3_2 = h * my_math_func2(res_list[i - 1][0], *y_list[i - 1])

            k4_1 = h * my_math_func1(res_list[i - 2][0], *y_list[i - 2])
            k4_2 = h * my_math_func1(res_list[i - 2][0], *y_list[i - 2])

            # correcting y1, y2 and y3
            res_list[i + 1][1] = res_list[i][1] + (9 * k1_1 + 19 * k2_1 - 5 * k3_1 + k4_1) / 24  # type: ignore
            res_list[i + 1][2] = res_list[i][2] + (9 * k1_2 + 19 * k2_2 - 5 * k3_2 + k4_2) / 24  # type: ignore

            if (abs(res_list[i + 1][1] - y_list[i + 1][0]) < h) and \
                    (abs(res_list[i + 1][2] - y_list[i + 1][1]) < h):
                break
            else:
                y_list[i + 1][0] = res_list[i + 1][1]
                y_list[i + 1][1] = res_list[i + 1][2]
                m += 1
    res_list = [(round(val[0], step_round), round(val[1], step_round), round(val[2], step_round)) for val in res_list]
    return res_list
