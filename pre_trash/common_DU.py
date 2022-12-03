from pre_trash.Supporting_Math_logic import Supporting_Math_logic as Support_Math


class Common_DU_Solving(Support_Math):
    '''All public methods return a list of[x, y]
    and get x_intial, x_end, y_intial ansd step_integrate'''
    @classmethod
    def _template_method(cls, method,  # pass method name (euler, runge_kutta4, etc...)
                         my_math_func,  # math function on what we working
                         # just info what passed in function
                         x_intial: float, x_end: float, y_intial: float,
                         step_integrate: float) -> list[tuple[float, float]]:
        '''Main(unic) function what realise logic of math metods'''

        """
        method is for instance eiler, runga_kutta etc.
        my_math_func is for instance x*math.cos((x**2 * y)/x-y)
        x_intial is the x0
        x_end is the x_k
        y_intial is the y0
        step_integrate is the eps or 'h'
        amount_points_integrate is the n"""
        step_round = cls._find_step_round(step_integrate)
        res_list: list[tuple[float, float]] = []
        amount_points_integrate = int((x_end - x_intial)/step_integrate)
        x_current = x_intial
        y_current = y_intial
        res_list.append((round(x_current, step_round),
                        round(y_current, step_round)))
        return method(my_math_func, step_integrate, step_round, res_list,
                      amount_points_integrate, x_current, y_current)

    @classmethod
    def euler(cls, my_math_func,
              x_intial: float, x_end: float, y_intial: float,
              step_integrate: float) -> list[tuple[float, float]]:
        return cls._template_method(cls._euler_logic, my_math_func, x_intial, x_end, y_intial, step_integrate)

    @classmethod
    def _euler_logic(cls, my_math_func,
                     step_integrate: float, step_round: int, res_list: list[tuple[float, float]],
                     amount_points_integrate: int, x_current: float, y_current: float
                     ) -> list[tuple[float, float]]:
        for i in range(amount_points_integrate):
            x_current += step_integrate
            y_current += step_integrate*my_math_func(x_current, y_current)
            res_list.append((round(x_current, step_round),
                            round(y_current, step_round)))
        return res_list

    @classmethod
    def runge_kutta4(cls, my_math_func,
                     x_intial: float, x_end: float, y_intial: float,
                     step_integrate: float) -> list[tuple[float, float]]:
        return cls._template_method(cls._runge_kutta4_logic, my_math_func, x_intial, x_end, y_intial, step_integrate)

    @classmethod
    def _runge_kutta4_logic(cls, my_math_func,
                            step_integrate: float, step_round: int, res_list: list[tuple[float, float]],
                            amount_points_integrate: int, x_current: float, y_current: float
                            ) -> list[tuple[float, float]]:
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

    @classmethod
    def runge_kutta5(cls, my_math_func,
                     x_intial: float, x_end: float, y_intial: float,
                     step_integrate: float) -> list[tuple[float, float]]:
        return cls._template_method(cls._runge_kutta5_logic, my_math_func, x_intial, x_end, y_intial, step_integrate)

    @classmethod
    def _runge_kutta5_logic(cls, my_math_func,
                            step_integrate: float, step_round: int, res_list: list[tuple[float, float]],
                            amount_points_integrate: int, x_current: float, y_current: float
                            ) -> list[tuple[float, float]]:

        for i in range(amount_points_integrate):
            x_current += step_integrate
            k0 = step_integrate*my_math_func(x_current, y_current)
            k1 = step_integrate * \
                my_math_func(x_current+step_integrate/3, y_current+k0/3)
            k2 = step_integrate * \
                my_math_func(x_current+step_integrate/3, y_current+k0/6+k1/6)
            k3 = step_integrate * \
                my_math_func(x_current+step_integrate/2, y_current+k0/8+3*k2/8)
            k4 = step_integrate * \
                my_math_func(x_current+step_integrate,
                             y_current+k0/2-3*k2/2+2*k3)
            y_current += (k0+4*k3+k4)/6
            res_list.append((round(x_current, step_round),
                            round(y_current, step_round)))

        return res_list

    @classmethod
    def adams_bashfort(cls, my_math_func,
                       x_intial: float, x_end: float, y_intial: float,
                       step_integrate: float) -> list[tuple[float, float]]:
        return cls._template_method(cls._adams_bashfort_logic, my_math_func, x_intial, x_end, y_intial, step_integrate)

    @classmethod
    def _adams_bashfort_logic(cls, my_math_func,
                              step_integrate: float, step_round: int, res_list: list[tuple[float, float]],
                              amount_points_integrate: int, x_current: float, y_current: float
                              ) -> list[tuple[float, float]]:
        for i in range(3):
            x_current += step_integrate
            k1 = step_integrate * my_math_func(x_current, y_current)
            k2 = step_integrate * \
                my_math_func(x_current+step_integrate/2, y_current+k1/2)
            k3 = step_integrate * \
                my_math_func(x_current+step_integrate/2, y_current+k2/2)
            k4 = step_integrate * \
                my_math_func(x_current+step_integrate, y_current+k3)
            y_current += (k1+2*k2+2*k3+k4)/6
            res_list.append((round(x_current, step_round),
                            round(y_current, step_round)))

        for i in range(3, amount_points_integrate):
            x_current += step_integrate
            k1 = step_integrate * my_math_func(x_current, y_current)
            k2 = step_integrate * \
                my_math_func(res_list[-1][0], res_list[-1][1])
            k3 = step_integrate * \
                my_math_func(res_list[-2][0], res_list[-2][1])
            k4 = step_integrate * \
                my_math_func(res_list[-3][0], res_list[-3][1])
            y_current += (55*k1-59*k2+37*k3-9*k4)/24
            res_list.append((round(x_current, step_round),
                            round(y_current, step_round)))

        return res_list

    @classmethod
    def adams_meulton(cls, my_math_func,
                      x_intial: float, x_end: float, y_intial: float,
                      step_integrate: float) -> list[tuple[float, float]]:
        return cls._template_method(cls._adams_meulton_logic, my_math_func, x_intial, x_end, y_intial, step_integrate)

    @classmethod
    def _adams_meulton_logic(cls, my_math_func,
                             step_integrate: float, step_round: int, res_list: list[tuple[float, float]],
                             amount_points_integrate: int, x_current: float, y_current: float
                             ) -> list[tuple[float, float]]:

        for i in range(3):
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

        for i in range(3, amount_points_integrate):
            x_current += step_integrate
            k1 = step_integrate * my_math_func(x_current, y_current)
            k2 = step_integrate * \
                my_math_func(res_list[-1][0], res_list[-1][1])
            k3 = step_integrate * \
                my_math_func(res_list[-2][0], res_list[-2][1])
            k4 = step_integrate * \
                my_math_func(res_list[-3][0], res_list[-3][1])
            y_current += (55*k1-59*k2+37*k3-9*k4)/24
            res_list.append((round(x_current, step_round),
                            round(y_current, step_round)))

        y_list = [el[1] for el in res_list]  # let's make copy of list y
        # res_list will contain x and y1
        res_list = [[pair[0], pair[1]] for pair in res_list]    # type: ignore
        # make res_list changeable
        for i in range(2, amount_points_integrate):
            for m in range(10):
                x_current = res_list[i][0]
                k1 = step_integrate * \
                    my_math_func(res_list[i+1][0], y_list[i+1])
                k2 = step_integrate * my_math_func(res_list[i][0], y_list[i])
                k3 = step_integrate * \
                    my_math_func(res_list[i-1][0], y_list[i-1])
                k4 = step_integrate * \
                    my_math_func(res_list[i-2][0], y_list[i-2])
                res_list[i+1][1] = res_list[i][1] + \
                    (9*k1+19*k2-5*k3+k4)/24  # type: ignore
                if abs(res_list[i+1][1]-y_list[i+1]) < step_integrate:
                    break
                else:
                    y_list[i+1] = res_list[i+1][1]
                    m += 1
        res_list = [(round(pair[0], step_round), round(
            pair[1], step_round)) for pair in res_list]
        return res_list
