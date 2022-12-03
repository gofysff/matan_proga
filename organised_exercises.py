import math_functions as mf
import du_solving_methods.du_1st_order as du_1ord
import du_solving_methods.du_3rd_order as du_3ord
import help_part as hp

# def second_exercise(my_math_func1=mf.my_func1_exersise1,
#                     my_math_func2=mf.my_func2_exersise2,
#                     x_0=2, x_k=7, y_0_0=0.2, y_0_1=-3, eps=0.0001, step_print=0.5) -> None:
#     '''function that organizes the decision of the second issue'''
#     print(
#         f"x_0 = {x_0}, y_0_0 = {y_0_0}, y_0_1 = {y_0_1}, x_k = {x_k}, epsilon = {eps}")

#     # '''let's create functions to solving system DU 1st grade by using decorator big_ord_sys.systemdu_1ord_grade'''
#     # res_eulier_func = big_ord_sys.systemdu_1ord_grade(
#     #     du_1ord.euler)
#     # res_runge_kutta4_func = big_ord_sys.systemdu_1ord_grade(
#     #     du_1ord.runge_kutta4)
#     # res_runge_kutta5_func = big_ord_sys.systemdu_1ord_grade(
#     #     du_1ord.runge_kutta5)
#     # res_adams_bashfort_func = big_ord_sys.systemdu_1ord_grade(
#     #     du_1ord.adams_bashfort)
#     # res_adams_meulton_func = big_ord_sys.systemdu_1ord_grade(
#     #     du_1ord.adams_meulton)

#     # '''let's create lists of [x, y_1, y_2] by every solving methods using craated functions'''
#     # res_eulier = res_eulier_func(
#     #     my_math_func1, my_math_func2, x_0, x_k, y_0_0, y_0_1, eps)
#     # res_runge_kutta4 = res_runge_kutta4_func(
#     #     my_math_func1, my_math_func2, x_0, x_k, y_0_0, y_0_1, eps)
#     # res_runge_kutta5 = res_runge_kutta5_func(
#     #     my_math_func1, my_math_func2, x_0, x_k, y_0_0, y_0_1, eps)
#     # res_adams_bashfort = res_adams_bashfort_func(
#     #     my_math_func1, my_math_func2, x_0, x_k, y_0_0, y_0_1, eps)
#     # res_adams_meulton = res_adams_meulton_func(
#     #     my_math_func1, my_math_func2, x_0, x_k, y_0_0, y_0_1, eps)

#     '''let's print the results'''
#     print('Solved by euler method')
#     du_1ord.pretty_print_result3el(res_eulier, step_print)
#     print('Solved by runge_kutta4 method')
#     du_1ord.pretty_print_result3el(res_runge_kutta4, step_print)
#     print('Solved by runge_kutta5 method')
#     du_1ord.pretty_print_result3el(res_runge_kutta5, step_print)
#     print('Solved by adams_bashfort method')
#     du_1ord.pretty_print_result3el(
#         res_adams_bashfort, step_print)
#     print('Solved by adams_meulton method')
#     du_1ord.pretty_print_result3el(
#         res_adams_meulton, step_print)


def first_exercise(x_0=1, x_k=6, y_0=-0.5, eps=0.0001, active_func=mf.my_func1_exersise1, step_showing=0.5) -> None:
    """function that organizes the decision of the first issue"""

    print(f"x_0 is {x_0}, y_0 is {y_0}, x_k is {x_k}, epsilon is {eps}")

    '''let's create lists of [x, y_1, y_2] by every solving methods using craated functions'''
    res_eulier = du_1ord.euler(active_func, x_0, x_k, y_0, eps)
    res_runge_kutta4 = du_1ord.runge_kutta4(
        active_func, x_0, x_k, y_0, eps)
    res_runge_kutta5 = du_1ord.runge_kutta5(
        active_func, x_0, x_k, y_0, eps)
    res_adams_bashfort = du_1ord.adams_bashfort(
        active_func, x_0, x_k, y_0, eps)
    res_adams_meult = du_1ord.adams_meulton(
        active_func, x_0, x_k, y_0, eps)

    '''let's print the results'''
    print('Solved by euler method')
    hp.pretty_print_el2(res_eulier, step_showing)
    print("Solved by runge-kutta4 method")
    hp.pretty_print_el2(
        res_runge_kutta4, step_showing)
    print("Solved by runge-kutta5 method")
    hp.pretty_print_el2(
        res_runge_kutta5, step_showing)
    print("Solved by adams-bashfort method")
    hp.pretty_print_el2(
        res_adams_bashfort, step_showing)
    print("Solved by adams-meulton method")
    hp.pretty_print_el2(
        res_adams_meult, step_showing)


def third_exercise(x_0=0, x_k=2, y_0_0=1, y_0_1=0, y_0_2=1, eps=0.0001, my_math_f1=mf.test1, my_math_f2=mf.test2,
                   my_math_f3=mf.test3, step_showing=0.2) -> None:
    """function that organizes the decision of the third issue"""

    print(f"x_0 is {x_0}, y_0_1 is {y_0_0}, y_0_2 is {y_0_1}, y_0_3 is {y_0_2} x_k is {x_k}, epsilon is {eps}")

    res_eulier = du_3ord.euler(my_math_f1, my_math_f2, my_math_f3, x_0, x_k, y_0_0, y_0_1, y_0_2, eps)
    res_runge_kutta4 = du_3ord.runge_kutta4(my_math_f1, my_math_f2, my_math_f3, x_0, x_k, y_0_0, y_0_1, y_0_2, eps)
    res_runge_kutta5 = du_3ord.runge_kutta5(my_math_f1, my_math_f2, my_math_f3, x_0, x_k, y_0_0, y_0_1, y_0_2, eps)
    res_adams_bashfort = du_3ord.adams_bashfort(my_math_f1, my_math_f2, my_math_f3, x_0, x_k, y_0_0, y_0_1, y_0_2, eps)
    res_adams_meult = du_3ord.adams_meulton(my_math_f1, my_math_f2, my_math_f3, x_0, x_k, y_0_0, y_0_1, y_0_2, eps,
                                            res_adams_bashfort=res_adams_bashfort)

    '''let's print the results'''
    print('Solved by euler method')
    hp.pretty_print_el4(res_eulier, step_showing)
    print("Solved by runge-kutta4 method")
    hp.pretty_print_el4(
        res_runge_kutta4, step_showing)
    print("Solved by runge-kutta5 method")
    hp.pretty_print_el4(
        res_runge_kutta5, step_showing)
    print("Solved by adams-bashfort method")
    hp.pretty_print_el4(
        res_adams_bashfort, step_showing)
    print("Solved by adams-meulton method")
    hp.pretty_print_el4(
        res_adams_meult, step_showing)
