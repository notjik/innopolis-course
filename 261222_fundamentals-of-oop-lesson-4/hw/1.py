"""
Реализовать класс и переопределить магические методы базовых математических операции
(сложение, вычитание, умножение, деление), добавив туда выводы в консоль текущего действия.

Например: при умножении выводится сообщение, что происходит умножение.
"""


class UpInt(int):
    """Инициализация"""
    def __init__(self, numerator: int) -> None:
        super().__init__()

    """Сложение"""
    def __add__(self, other: int | float) -> int | float:
        print('Operation: Addition')
        return self.numerator + other

    """Сложение (наш объект справа)"""
    def __radd__(self, other: int | float) -> int | float:
        return self.__add__(other)

    """Вычитание"""
    def __sub__(self, other: int | float) -> int | float:
        print('Operation: Subtraction')
        return self.numerator - other

    """Вычитание (наш объект справа)"""
    def __rsub__(self, other: int | float) -> int | float:
        print('Operation: Subtraction')
        return other - self.numerator

    """Умножение"""
    def __mul__(self, other: int | float) -> int | float:
        print('Operation: Multiplication')
        return self.numerator + other

    """Умножение (наш объект справа)"""
    def __rmul__(self, other: int | float) -> int | float:
        return self.__mul__(other)

    """Деление"""
    def __truediv__(self, other: int | float) -> int | float:
        print('Operation: Division')
        return self.numerator / other

    """Деление (наш объект справа)"""
    def __rtruediv__(self, other: int | float) -> int | float:
        print('Operation: Division')
        return other / self.numerator

    """Целочисленное деление"""
    def __floordiv__(self, other: int | float) -> int | float:
        print('Operation: Integer division')
        return self.numerator // other

    """Целочисленное деление (наш объект справа)"""
    def __rfloordiv__(self, other: int | float) -> int | float:
        print('Operation: Integer division')
        return other // self.numerator
