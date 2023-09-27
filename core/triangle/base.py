def may_be_triangle(a: float, b: float, c: float) -> bool:
    if a > c:
        a, c = c, a

    if b > c:
        b, c = c, b

    return all(map(lambda x: x > 0, [a, b, c])) and c < a + b


def get_area(a: float, b: float, c: float) -> float:
    if may_be_triangle(a, b, c) is False:
        raise ValueError('It is not triangle')
    
    p = (a + b + c) / 2

    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
