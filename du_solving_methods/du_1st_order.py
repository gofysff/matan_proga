import help_part as hp

'''All public methods return a list of[x, y]
and get x0, x_k, y_0 ansd h'''


def euler(my_math_func,
          x0: float, x_k: float, y_0: float,
          h: float) -> list[tuple[float, float]]:
    step_round = hp.find_step_round(h)
    res_list: list[tuple[float, float]] = []
    amount_points = int((x_k - x0)/h)
    x_i = x0
    y_i = y_0
    res_list.append((round(x_i, step_round),
                     round(y_i, step_round)))
    for i in range(amount_points):
        x_i += h
        y_i += h*my_math_func(x_i, y_i)
        res_list.append((round(x_i, step_round),
                        round(y_i, step_round)))
    return res_list


def runge_kutta4(my_math_func,
                 x0: float, x_k: float, y_0: float,
                 h: float) -> list[tuple[float, float]]:
    step_round = hp.find_step_round(h)
    res_list: list[tuple[float, float]] = []
    amount_points = int((x_k - x0)/h)
    x_i = x0
    y_i = y_0
    res_list.append((round(x_i, step_round),
                     round(y_i, step_round)))
    for i in range(amount_points):
        x_i += h
        k1 = h*my_math_func(x_i, y_i)
        k2 = h * \
            my_math_func(x_i+h/2, y_i+k1/2)
        k3 = h * \
            my_math_func(x_i+h/2, y_i+k2/2)
        k4 = h * \
            my_math_func(x_i+h, y_i+k3)
        y_i += (k1+2*k2+2*k3+k4)/6
        res_list.append((round(x_i, step_round),
                         round(y_i, step_round)))
    return res_list


def runge_kutta5(my_math_func,
                 x0: float, x_k: float, y_0: float,
                 h: float) -> list[tuple[float, float]]:
    step_round = hp.find_step_round(h)
    res_list: list[tuple[float, float]] = []
    amount_points = int((x_k - x0)/h)
    x_i = x0
    y_i = y_0
    res_list.append((round(x_i, step_round),
                     round(y_i, step_round)))
    for i in range(amount_points):
        x_i += h
        k0 = h*my_math_func(x_i, y_i)
        k1 = h * \
            my_math_func(x_i+h/3, y_i+k0/3)
        k2 = h * \
            my_math_func(x_i+h/3, y_i+k0/6+k1/6)
        k3 = h * \
            my_math_func(x_i+h/2, y_i+k0/8+3*k2/8)
        k4 = h * \
            my_math_func(x_i+h,
                         y_i+k0/2-3*k2/2+2*k3)
        y_i += (k0+4*k3+k4)/6
        res_list.append((round(x_i, step_round),
                        round(y_i, step_round)))
    return res_list


def adams_bashfort(my_math_func,
                   x0: float, x_k: float, y_0: float,
                   h: float) -> list[tuple[float, float]]:
    step_round = hp.find_step_round(h)
    res_list: list[tuple[float, float]] = []
    amount_points = int((x_k - x0)/h)
    x_i = x0
    y_i = y_0
    res_list.append((round(x_i, step_round),
                     round(y_i, step_round)))
    for i in range(3):
        x_i += h
        k1 = h * my_math_func(x_i, y_i)
        k2 = h * \
            my_math_func(x_i+h/2, y_i+k1/2)
        k3 = h * \
            my_math_func(x_i+h/2, y_i+k2/2)
        k4 = h * \
            my_math_func(x_i+h, y_i+k3)
        y_i += (k1+2*k2+2*k3+k4)/6
        res_list.append((round(x_i, step_round),
                        round(y_i, step_round)))

    for i in range(3, amount_points):
        x_i += h
        k1 = h * my_math_func(x_i, y_i)
        k2 = h * \
            my_math_func(res_list[-1][0], res_list[-1][1])
        k3 = h * \
            my_math_func(res_list[-2][0], res_list[-2][1])
        k4 = h * \
            my_math_func(res_list[-3][0], res_list[-3][1])
        y_i += (55*k1-59*k2+37*k3-9*k4)/24
        res_list.append((round(x_i, step_round),
                        round(y_i, step_round)))
    return res_list


def adams_meulton(my_math_func,
                  x0: float, x_k: float, y_0: float,
                  h: float) -> list[tuple[float, float]]:
    step_round = hp.find_step_round(h)
    res_list: list[tuple[float, float]] = []
    amount_points = int((x_k - x0)/h)
    x_i = x0
    y_i = y_0

    for i in range(3):
        x_i += h
        k1 = h*my_math_func(x_i, y_i)
        k2 = h * \
            my_math_func(x_i+h/2, y_i+k1/2)
        k3 = h * \
            my_math_func(x_i+h/2, y_i+k2/2)
        k4 = h * \
            my_math_func(x_i+h, y_i+k3)
        y_i += (k1+2*k2+2*k3+k4)/6
        res_list.append((round(x_i, step_round),
                        round(y_i, step_round)))

    for i in range(3, amount_points):
        x_i += h
        k1 = h * my_math_func(x_i, y_i)
        k2 = h * \
            my_math_func(res_list[-1][0], res_list[-1][1])
        k3 = h * \
            my_math_func(res_list[-2][0], res_list[-2][1])
        k4 = h * \
            my_math_func(res_list[-3][0], res_list[-3][1])
        y_i += (55*k1-59*k2+37*k3-9*k4)/24
        res_list.append((round(x_i, step_round),
                        round(y_i, step_round)))

    y_list = [el[1] for el in res_list]  # let's make copy of list y
    # res_list will contain x and y1
    res_list = [[pair[0], pair[1]] for pair in res_list]    # type: ignore
    # make res_list changeable
    for i in range(2, amount_points-1):
        for m in range(10):
            x_i = res_list[i][0]
            k1 = h * my_math_func(res_list[i+1][0], y_list[i+1])
            k2 = h * my_math_func(res_list[i][0], y_list[i])
            k3 = h * my_math_func(res_list[i-1][0], y_list[i-1])
            k4 = h * my_math_func(res_list[i-2][0], y_list[i-2])
            res_list[i+1][1] = res_list[i][1] + \
                (9*k1+19*k2-5*k3+k4)/24  # type: ignore
            if abs(res_list[i+1][1]-y_list[i+1]) < h:
                break
            else:
                y_list[i+1] = res_list[i+1][1]
                m += 1
    res_list = [(round(pair[0], step_round), round(pair[1], step_round))
                for pair in res_list]
    return res_list
