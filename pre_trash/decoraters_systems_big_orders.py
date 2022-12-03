# def systemDu_1st_grade(method_solving_du):
#     '''decorator for making method(for solving only one du) good for solving systems du'''
#     def wrapper(  # method_solving_du like euler, runge_kutta4 etc
#             math_func1, math_func2,  # like cos(x+y2) and sin(x+y1)
#             x_intial: float, x_end: float, y_intial_0: float, y_intial_1: float,
#             step_integrate: float) -> list[tuple[float, float, float]]:
#         '''return a list of [x, y_1, y2]'''
#         first_res_array: list[tuple[float, float]] = method_solving_du(
#             math_func1, x_intial, x_end, y_intial_0, step_integrate)
#         second_res_array: list[tuple[float, float]] = method_solving_du(
#             math_func2, x_intial, x_end, y_intial_1, step_integrate)
#         res_list: list[tuple[float, float, float]] = [
#             (first_res_array[i][0], first_res_array[i][1], second_res_array[i][1]) for i in range(len(first_res_array))]
#         return res_list
#     return wrapper


# def systemDu_2nd_grade(method_solving_du):
#     '''decorator for making method(for solving only one du) good for solving systems du'''
#     def wrapper(  # method_solving_du like euler, runge_kutta4 etc
