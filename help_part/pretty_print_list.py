import math


def pretty_print_el4(lt_values: list[tuple[float, float, float, float]], step_show: float) -> None:
    if step_show <= 1:  # avoiding math with float values
        step_exponentiate = math.floor(math.log10(1/step_show))+1
    else:
        step_exponentiate = 0

    if (lt_values[0][0] * 10**step_exponentiate) % (step_show * 10**step_exponentiate) != 0:
        # print edge values if they are not in step_show
        print(f"x = {lt_values[0][0]:5.5f},\ty1 = {lt_values[0][1]:5.8f}\ty2 = "
              f"{lt_values[0][2]:5.8f}\ty3 = {lt_values[0][3]:5.8f}")

    for x, y1, y2, y3 in lt_values:
        if (x * 10**step_exponentiate) % (step_show * 10**step_exponentiate) == 0:
            print(f"x = {x:5.8f},\t y1 = {y1:5.8f},\t y2 = {y2:5.8f},\t y3 = {y3:5.8f}")

    if (lt_values[-1][0] * 10**step_exponentiate) % (step_show * 10**step_exponentiate) != 0:
        # print edge values if they are not in step_show
        print(f"x = {lt_values[-1][0]:5.8f},\ty1"
              f" = {lt_values[-1][1]:5.8f}\ty2 = {lt_values[-1][2]:5.8f}\ty3 = {lt_values[-1][3]:5.8f}")


def pretty_print_el3(lt_values: list[tuple[float, float, float]], step_show: float) -> None:
    if step_show <= 1:  # avoiding math with float values
        step_exponentiate = math.floor(math.log10(1/step_show))+1
    else:
        step_exponentiate = 0

    if (lt_values[0][0] * 10**step_exponentiate) % (step_show * 10**step_exponentiate) != 0:
        # print edge values if they are not in step_show
        print(f"x = {lt_values[0][0]:5.8f},\ty1 = {lt_values[0][1]:5.8f}\ty2 = {lt_values[0][2]:5.8f}")

    for x, y1, y2 in lt_values:
        if (x * 10**step_exponentiate) % (step_show*10**step_exponentiate) == 0:
            print(f"x = {x:5.8f},\t y1 = {y1:5.8f},\t y2 = {y2:5.8f}")

    if (lt_values[-1][0] * 10 ** step_exponentiate) % (step_show * 10 ** step_exponentiate) != 0:
        # print edge values if they are not in step_show
        print(f"x = {lt_values[-1][0]:5.8f},\ty1"
              f" = {lt_values[-1][1]:5.8f}\ty2 = {lt_values[-1][2]:5.8f}\t")


def pretty_print_el2(lt_values: list[tuple[float, float]], step_show: float) -> None:
    if step_show <= 1:  # avoiding math with float values
        step_exponentiate = math.floor(math.log10(1/step_show))+1
    else:
        step_exponentiate = 0

    if(lt_values[0][0] * 10 ** step_exponentiate) % (step_show * 10 ** step_exponentiate) != 0:
        # print edge values if they are not in step_show
        print(f"x = {lt_values[0][0]:5.8f},\ty = {lt_values[0][1]:5.8f}\t")

    for x, y in lt_values:
        if (x * 10**step_exponentiate) % (step_show*10**step_exponentiate) == 0:
            print(f"x = {x:5.8f},\t y = {y:5.8f}")

    if (lt_values[-1][0] * 10 ** step_exponentiate) % (step_show * 10 ** step_exponentiate) != 0:
        # print edge values if they are not in step_show
        print(f"x = {lt_values[-1][0]:5.8f},\ty = {lt_values[-1][1]:5.8f}\t")
