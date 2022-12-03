import math


def find_step_round(step_integrate: float) -> int:
    '''step integrate is eps'''
    return int(math.log10(1/step_integrate))
