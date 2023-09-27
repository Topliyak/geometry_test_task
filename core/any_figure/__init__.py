from .. import (
    rect,
    circle,
    triangle,
)


figure_and_area_func = {
    'rect': rect.get_area,
    'circle': circle.get_area,
    'triangle': triangle.get_area,
}

figure_and_define_func = {
    'rect': rect.may_be_rect,
    'circle': circle.may_be_circle,
    'triangle': triangle.may_be_triangle,
}


def get_area(*sides) -> float | None:
    for figure in figure_and_define_func:
        is_figure_func = figure_and_define_func[figure]

        if len(is_figure_func.__annotations__) - 1 != len(sides):
            continue

        if is_figure_func(*sides):
            area_func = figure_and_area_func[figure]
            return area_func(*sides)

    return None
