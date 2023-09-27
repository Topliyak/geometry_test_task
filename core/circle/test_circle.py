from . import (
    get_area,
    may_be_circle,
)

import pytest


@pytest.mark.parametrize('r,correct', [
    [1, True],
    [0, False],
    [-0.1, False],
    [0.1, True],
])
def test_may_be_circle(r, correct):
    res = may_be_circle(r)
    assert res is correct


@pytest.mark.parametrize('radius,correct', [
    [1, 3.141593],
    [2, 12.566371],
    [10.112, 321.235841],
])
def test_get_area(radius, correct):
    res = get_area(radius)
    assert abs(res - correct) < 0.0001, f'Expected {correct}, but got {res}'


@pytest.mark.parametrize('r', [
    -1,
    -100,
    -1.1,
])
def test_get_area_fail(r):
    with pytest.raises(ValueError):
        get_area(r)
