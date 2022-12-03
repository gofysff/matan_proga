import math


class Supporting_Math_logic:
    @staticmethod
    def _find_step_round(step_integrate: float) -> int:
        '''step integrate is eps'''
        return int(math.log10(1/step_integrate))

    @staticmethod
    def pretty_print_result2el(res_lt: list[tuple[float, float]], step_print) -> None:
        '''one dimensional list with tuple of 2 floats'''
        for val in res_lt:
            if val[0] % step_print == 0:
                print(f'x is {val[0]:5}\ty is {val[1]:7}')
        print('\n\n')

    @staticmethod
    def pretty_print_result3el(res_lt: list[tuple[float, float, float]], step_print) -> None:
        '''one dimensional list with tuple of 2 floats'''
        for val in res_lt:
            if val[0] % step_print == 0:
                print(f'x is {val[0]:5}\ty1 is {val[1]:7}\ty2 is {val[2]:7}')
        print('\n\n')\


    @staticmethod
    def pretty_print_result4el(res_lt: list[tuple[float, float, float, float]], step_print) -> None:
        '''one dimensional list with tuple of 2 floats'''
        for val in res_lt:
            if val[0] % step_print == 0:
                print(
                    f'x is {val[0]:5}\ty1 is {val[1]:7}\ty2 is {val[2]:7}\ty3 is {val[3]:7}')
        print('\n\n')


if __name__ == '__main__':
    print(math.floor(math.log10(1/0.002)))
    print(math.floor(math.log10(1/0.001)))
    print(math.floor(math.log10(2)))
    print(math.floor(math.log10(0.29)))
    print(math.floor(1.0))
    print(math.floor(1.01))
    print(math.floor(1.99))
