def add(num1: int | float, num2: int | float) -> int | float:
    return num1 + num2


def sub(num1: int | float, num2: int | float) -> int | float:
    return num1 - num2


def mul(num1: int | float, num2: int | float) -> int | float:
    return num1 * num2


def div(num1: int | float, num2: int | float) -> float:
    try:
        return num1 / num2
    except ZeroDivisionError:
        return float("inf")


def power(num1: int | float, num2: int | float) -> int | float:
    return num1**num2
