"""
>>> p1 = Quantitie(5, 'm')
>>> p2 = Quantitie(10, 'm')
>>> p3 = p1 + p2
>>> print(p3.cords)
(15, 'm')
>>> p4 = Quantitie(2, 'm/s')
>>> try:
...     p5 = p1 + p4
... except AttributeError:
...     print('A')
A
>>> p6 = p1 * p4
>>> print(p6.cords)
(10, 'm.m/s')
>>> p7 = p6 * 2
>>> print(p7.cords)
(20, 'm.m/s')
"""


class Quantitie:
    def __init__(self, value: float, unit: str):
        self.unit = unit
        self.value = value
        self.cords = (self.value, self.unit)

    def __add__(self, other):
        if self.unit != other.unit:
            raise AttributeError
        return Quantitie(self.value + other.value, self.unit)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            value = self.value * other
            return Quantitie(value, self.unit)
        return Quantitie(self.value * other.value, f'{self.unit}.{other.unit}')
