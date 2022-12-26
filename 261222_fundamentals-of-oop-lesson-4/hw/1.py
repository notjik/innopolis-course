"""
Реализовать класс и переопределить магические методы базовых математических операции
(сложение, вычитание, умножение, деление), добавив туда выводы в консоль текущего действия.

Например: при умножении выводится сообщение, что происходит умножение.
"""


class UpInt(int):
    """Инициализация"""
    def __init__(self, n: int) -> None:
        super().__init__()
        self.i = n

    """Сложение"""
    def __add__(self, other: int | float) -> int | float:
        print('Operation: Addition')
        return self.i + other

    """Сложение (наш объект справа)"""
    def __radd__(self, other: int | float) -> int | float:
        return self.__add__(other)

    """Вычитание"""
    def __sub__(self, other: int | float) -> int | float:
        print('Operation: Subtraction')
        return self.i - other

    """Вычитание (наш объект справа)"""
    def __rsub__(self, other: int | float) -> int | float:
        print('Operation: Subtraction')
        return other - self.i

    """Умножение"""
    def __mul__(self, other: int | float) -> int | float:
        print('Operation: Multiplication')
        return self.i + other

    """Умножение (наш объект справа)"""
    def __rmul__(self, other: int | float) -> int | float:
        return self.__mul__(other)

    """Деление"""
    def __truediv__(self, other: int | float) -> int | float:
        print('Operation: Division')
        return self.i / other

    """Деление (наш объект справа)"""
    def __rtruediv__(self, other: int | float) -> int | float:
        print('Operation: Division')
        return other / self.i

    """Целочисленное деление"""
    def __floordiv__(self, other: int | float) -> int | float:
        print('Operation: Integer division')
        return self.i // other

    """Целочисленное деление (наш объект справа)"""
    def __rfloordiv__(self, other: int | float) -> int | float:
        print('Operation: Integer division')
        return other // self.i



