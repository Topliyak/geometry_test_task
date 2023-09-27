from . import (
    get_area,
    may_be_rect,
)

from .adventure import (
    is_square,
)

import pytest


@pytest.mark.parametrize('a,b,c,d,correct', [
    [1, 2, 2, 2, False],
    [1, 2, 2, 1, True],
    [1, 1, 1, 1, True],
    [1, 2, 3, 4, False],
    [-1, -1, -1, -1, False]
])
def test_may_be_rect(a, b, c, d, correct):
    res = may_be_rect(a, b, c, d)
    assert res is correct, f'Expected {correct}, but got {res}'


@pytest.mark.parametrize('a,b,c,d,correct', [
    [1, 2, 2, 1, 2],
    [11, 12, 11, 12, 132],
    [5.12, 6.3, 5.12, 6.3, 32.256]
])
def test_get_area(a, b, c, d, correct):
    res = get_area(a, b, c, d)
    assert (res - correct) < 0.0001, f'Expected {correct}, but got {res}'


@pytest.mark.parametrize('a,b,c,d', [
    [1, -2, 3, 4],
    [-0.1, -0.1, -0.1, -0.1]
])
def test_get_area_fail(a, b, c, d):
    with pytest.raises(ValueError):
        get_area(a, b, c, d)


@pytest.mark.parametrize('a,b,c,d,correct', [
    [1, 2, 2, 1, False],
    [2, 2, 2, 2, True],
    [3.11, 3.11, 3.12, 3.12, False],
])
def test_is_square(a, b, c, d, correct):
    res = is_square(a, b, c, d)
    assert res is correct, f'Expected {correct}, but got {res}'
