from . import (
    get_area,
)

import pytest


@pytest.mark.parametrize('sides,correct', [
    [[1, 2, 2, 1], 2],
    [[2, 2, 1], 0.968246],
    [[1, 2, 1], None],
    [[11.445], 411.511017],
    [[1, 2, 3, 4], None],
])
def test_get_area(sides, correct):
    res = get_area(*sides)
    assert res == correct == None or abs(res - correct) < 0.00001
