def Euler(my_math_func, x_0: float, x_k: float, y_0: float,
          step_integrate: float) -> list[tuple[float, float]]:
    """
     is the x0
    x_k is the x_k
    y_0 is the y0
    step_integrate is the eps
    amount_points_integrate is the n"""
    # step_round = find_step_round(step_integrate)
    step_round = 3
    res_list: list[tuple[float, float]] = []
    amount_points_integrate = int((x_k - x_0)/step_integrate)
    x_current = x_0
    y_current = y_0
    res_list.append((round(x_current, step_round),
                    round(y_current, step_round)))

    for i in range(amount_points_integrate):
        x_current += step_integrate
        y_current += step_integrate*my_math_func(x_current, y_current)
        res_list.append((round(x_current, step_round),
                        round(y_current, step_round)))
    return res_list
