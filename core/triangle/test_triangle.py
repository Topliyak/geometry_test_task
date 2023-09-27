from . import (
    get_area,
    may_be_triangle,
)

from .adventure import (
    is_right_triangle,
)

import pytest


@pytest.mark.parametrize('a,b,c,correct', [
    [1, 2, 33, False],
    [1, 2, 3, False],
    [10, 20, 21, True],
    [-10, 20, 21, False],
    [2, 5, 6, True],
])
def test_may_be_triangle(a, b, c, correct):
    res = may_be_triangle(a, b, c)
    assert res is correct


@pytest.mark.parametrize('a,b,c,correct', [
    [1, 3, 3, 1.47902],
    [10, 20, 21, 98.906206]
])
def test_get_area(a, b, c, correct):
    res = get_area(a, b, c)
    assert abs(res - correct) < 0.0001, f'Expected {correct}, but got {res}'


@pytest.mark.parametrize('a,b,c', [
    [1, 2, 3]
])
def test_get_area_fail(a, b, c):
    with pytest.raises(ValueError):
        get_area(a, b, c)


@pytest.mark.parametrize('a,b,c,correct', [
    [1, 6, 6, False],
    [3, 4, 5, True]
])
def test_is_right_triangle(a, b, c, correct):
    res = is_right_triangle(a, b, c)
    assert res is correct, f'Expected {correct}, but got {res}'


@pytest.mark.parametrize('a,b,c', [
    [1, 2, 3],
    [1, 5, 6],
])
def test_is_right_triangle_fail(a, b, c):
    with pytest.raises(ValueError):
        is_right_triangle(a, b, c)
