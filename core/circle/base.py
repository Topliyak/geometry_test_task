from math import pi


def may_be_circle(radius: float) -> bool:
    return radius > 0


def get_area(radius: float) -> float:
    if may_be_circle(radius) is False:
        raise ValueError('It is not circle')
    
    return pi * radius**2
