"""
Создать декоратор, измеряющий время выполнения функции. Для расчета времени ознакомьтесь с модулем datetime.
"""
from time import perf_counter
from typing import Callable, Any


def func_timer(func: Callable) -> Any:
    def wrapper(*args, **kwargs) -> Any:
        start = perf_counter()
        call = func(*args, **kwargs)
        print('Function «{}» was completed in {} second!\n'.format(func.__name__, perf_counter() - start))
        return call

    return wrapper
