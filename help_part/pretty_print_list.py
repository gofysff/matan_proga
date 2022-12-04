import math


def pretty_print_el4(lt_values: list[tuple[float, float, float, float]], step_show: float) -> None:
    if step_show <= 1:  # avoiding math with float values
        step_exponentiate = math.floor(math.log10(1/step_show))+1
    else:
        step_exponentiate = 0

    if (lt_values[0][0] * 10**step_exponentiate) % (step_show * 10**step_exponentiate) == 0:
        # print edge values if they are not in step_show
        print(f"x = {lt_values[0][0]:5},\ty1 = {lt_values[0][1]}\ty2 = {lt_values[0][2]}\ty3 = {lt_values[0][3]}")
    for x, y1, y2, y3 in lt_values:
        if (x * 10**step_exponentiate) % (step_show * 10**step_exponentiate) == 0:
            print(f"x = {x:5},\t y1 = {y1:-8},\t y2 = {y2:8},\t y3 = {y3:8}")
    if (lt_values[-1][0] * 10**step_exponentiate) % (step_show * 10**step_exponentiate) == 0:
        # print edge values if they are not in step_show
        print(f"x = {lt_values[-1][0]:5},\ty1"
              f" = {lt_values[-1][1]:8}\ty2 = {lt_values[-1][2]:8}\ty3 = {lt_values[-1][3]:8}")


def pretty_print_el3(lt_values: list[tuple[float, float, float]], step_show: float) -> None:
    if step_show <= 1:  # avoiding math with float values
        step_exponentiate = math.floor(math.log10(1/step_show))+1
    else:
        step_exponentiate = 0

    if (lt_values[0][0] * 10**step_exponentiate) % (step_show * 10**step_exponentiate) == 0:
        # print edge values if they are not in step_show
        print(f"x = {lt_values[0][0]:5},\ty1 = {lt_values[0][1]}\ty2 = {lt_values[0][2]}")
    for x, y1, y2 in lt_values:
        if (x * 10**step_exponentiate) % (step_show*10**step_exponentiate) == 0:
            print(f"x = {x:-5},\t y1 = {y1:-8},\t y2 = {y2:-8}")
    if (lt_values[-1][0] * 10 ** step_exponentiate) % (step_show * 10 ** step_exponentiate) == 0:
        # print edge values if they are not in step_show
        print(f"x = {lt_values[-1][0]:5},\ty1"
              f" = {lt_values[-1][1]:8}\ty2 = {lt_values[-1][2]:8}\t")


def pretty_print_el2(lt_values: list[tuple[float, float]], step_show: float) -> None:
    if step_show <= 1:  # avoiding math with float values
        step_exponentiate = math.floor(math.log10(1/step_show))+1
    else:
        step_exponentiate = 0

    if(lt_values[0][0] * 10 ** step_exponentiate) % (step_show * 10 ** step_exponentiate) == 0:
        # print edge values if they are not in step_show
        print(f"x = {lt_values[0][0]:5},\ty = {lt_values[0][1]}\t")
    for x, y in lt_values:
        if (x * 10**step_exponentiate) % (step_show*10**step_exponentiate) == 0:
            print(f"x = {x:5},\t y = {y:8}")
    if (lt_values[-1][0] * 10 ** step_exponentiate) % (step_show * 10 ** step_exponentiate) == 0:
        # print edge values if they are not in step_show
        print(f"x = {lt_values[-1][0]:5},\ty = {lt_values[-1][1]:8}\t")