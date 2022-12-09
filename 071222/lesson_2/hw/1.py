"""
Написать функцию isPrime, которая принимает число и возвращает простое число или нет.
"""


def isPrime(x: int) -> bool:
    if x < 2:
        return False
    i = 2
    while i ** 2 < x:
        if x % i == 0:
            return False
        i += 1
    return True

