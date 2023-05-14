import sympy as sp

coeficients_n = {
    2: [-0.577340, 0.577360],
    3: [-0.707207, 0, 0.707207],
    4: [-0.794653, -0.187591, 0.187591, 0.794653],
    5: [-0.832497, -0.374542, 0, 0.374542, 0.832497],
    6: [-0.866246, -0.422518, -0.266634, 0.266634, 0.422518, 0.866248],
    7: [-0.883861, -0.529656, -0.323913, 0, 0.323913, 0.529656, 0.883861],
    9: [-0.911579, -0.601029, -0.528761, -0.167905, 0, 0.167905, 0.528761, 0.601018, 0.911579]
}


def chebishev(func, a: float, b: float, n=9) -> float:
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

    # coef plus for all points
    t_coef1 = (b+a)/2

    # coef multipl for all points
    t_coef2 = (b-a)/2

    # calculate points
    points_t = [t_coef1+t_coef2*x for x in coeficients]

    # general coef
    general_coef = (b-a)/n
    return general_coef*sum([func.evalf(subs={x: points_t[i]}) for i in range(n)])


def print_results(chebishev, x, f, a, b):

    print(f'Функция {f} c пределами {a}:{b}')
    # print sympy integral from a to b
    print('Посчитано при помощи формулы Ньютона-Лейбница')
    print(sp.integrate(f, (x)).evalf(
        subs={x: b}) - sp.integrate(f, (x)).evalf(subs={x: a}), end="\n\n")
    print('Посчитано при помощи формул Чебышева')

    for i in range(2, 7+1):
        print(f'Результат при n = {i} {chebishev(f, a, b, n =i)}')
    print(f'Результат при n = 9 {chebishev(f, a, b)}')


if __name__ == "__main__":
    x = sp.symbols('x')

    f = sp.sin(x) ** 4
    a = 0
    b = 2
    print_results(chebishev, x, f, a, b)
    print("\n\n")

    f = sp.sqrt(2*x-1)
    a = 5
    b = 13
    print_results(chebishev, x, f, a, b)
