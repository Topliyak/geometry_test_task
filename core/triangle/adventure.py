from . import may_be_triangle
from math import isclose


def is_right_triangle(a: float, b: float, c: float) -> bool:
    if may_be_triangle(a, b, c) is False:
        raise ValueError('It is not triangle')
    
    if a > c:
        a, c = c, a

    if b > c:
        b, c = c, b

    return isclose(a ** 2 + b ** 2, c ** 2)
