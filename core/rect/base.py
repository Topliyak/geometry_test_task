from collections import Counter


def may_be_rect(a: float, b: float, c: float, d: float) -> bool:
    sides = [a, b, c, d]
    counts = Counter(sides)
    all_positive = all(map(lambda x: x > 0, sides))

    return all_positive and (len(counts) == 1 or len(counts) == 2 and counts[a] == 2)


def get_area(a: float, b: float, c: float, d: float):
    if may_be_rect(a, b, c, d) is False:
        raise ValueError('It is not rect')
    
    sides = [a, b, c, d]
    return min(sides) * max(sides)
