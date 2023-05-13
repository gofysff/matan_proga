import sympy as sp

coeficients_n = {
    2: [-0.577340, 0.577360],
    3: [-0.707207, 0, -0.707207],
    4: [-0.794653, -0.187591, 0.187591, 0.794653],
    5: [-0.832497, -0.374542, 0, 0.374542, 0.832497],
    6: [-0.866246, -0.422518, -0.266634, 0.266634, 0.422518, 0.866248],
    7: [-0.883861, -0.529656, -0.323913, 0, 0.323913, 0.529656, 0.883861],
    9: [-0.911579, -0.601029, -0.528761, -0.167905, 0, 0.167905, 0.528761, 0.601018, 0.911579]
}


def chebishev(func, a: float, b: float, n: int) -> float:
    """
    :param func: function to integrate
    :param a: lower limit
    :param b: upper limit
    :param n: number of points
    :return: integral
    """
    x = sp.symbols('x')
    # Calculate the coeficients
    coeficients = coeficients_n[n]

    # coef for all points
    t_coef = (b+a)/2*(b-a)/2

    # calculate points
    points_t = [t_coef*x for x in coeficients]

    # general coef
    general_coef = (b-a)/n
    return general_coef*sum([func.evalf(subs={x: points_t[i]}) for i in range(n)])


if __name__ == "__main__":
    x = sp.symbols('x')
    # f = sin(x)^4
    f = sp.sin(x) ** 4
    print(type(f))
    a = 0
    b = 2
    n = 9
    print(chebishev(f, a, b, n))
    # print sympy integral from a to b
    print(sp.integrate(f, (x)).evalf(
        subs={x: b}) - sp.integrate(f, (x)).evalf(subs={x: a}))
