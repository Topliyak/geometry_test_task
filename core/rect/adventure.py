from . import may_be_rect


def is_square(a: float, b: float, c: float, d: float) -> bool:
    if may_be_rect(a, b, c, d) is False:
        raise ValueError('It is not rect')
    
    return len({a, b, c, d}) == 1
