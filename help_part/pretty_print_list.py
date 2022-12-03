import math


def pretty_print_el4(lt_values: list[tuple[float, float, float, float]], step_show: float) -> None:
    if step_show <= 1:  # avoiding math with float values
        step_exponentiate = math.floor(math.log10(1/step_show))+1
    else:
        step_exponentiate = 0
    for x, y1, y2, y3 in lt_values:
        if (x * 10**step_exponentiate) % (step_show * 10**step_exponentiate) == 0:
            print(f"x = {x:5}, y1 = {y1:-8}, y2 = {y2:8}, y3 = {y3:-8}")


def pretty_print_el3(lt_values: list[tuple[float, float, float]], step_show: float) -> None:
    if step_show <= 1:  # avoiding math with float values
        step_exponentiate = math.floor(math.log10(1/step_show))+1
    else:
        step_exponentiate = 0
    for x, y1, y2 in lt_values:
        if (x * 10**step_exponentiate) % (step_show*10**step_exponentiate) == 0:
            print(f"x = {x:-5}, y1 = {y1:-8}, y2 = {y2:-8}")


def pretty_print_el2(lt_values: list[tuple[float, float]], step_show: float) -> None:
    if step_show <= 1:  # avoiding math with float values
        step_exponentiate = math.floor(math.log10(1/step_show))+1
    else:
        step_exponentiate = 0
    for x, y in lt_values:
        if (x * 10**step_exponentiate) % (step_show*10**step_exponentiate) == 0:
            print(f"x = {x:5}, y = {y:8}")
