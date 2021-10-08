import numpy as np
import pytest

from sdia_python.lab2.box_window import BoxWindow, UnitBoxWindow
from sdia_python.lab2.ball_window import BallWindow


def test_raise_type_error_when_something_is_called():
    with pytest.raises(TypeError):
        # call_something_that_raises_TypeError()
        raise TypeError()


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[2.5, 2.5]]), "BoxWindow: [2.5, 2.5]"),
        (np.array([[0, 5], [0, 5]]), "BoxWindow: [0, 5] x [0, 5]"),
        (
            np.array([[0, 5], [-1.45, 3.14], [-10, 10]]),
            "BoxWindow: [0.0, 5.0] x [-1.45, 3.14] x [-10.0, 10.0]",
        ),
    ],
)
def test_box_string_representation(bounds, expected):
    assert str(BoxWindow(bounds)) == expected


@pytest.fixture
def box_2d_05():
    return BoxWindow(np.array([[0, 5], [0, 5]]))


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([0, 0]), True),
        (np.array([2.5, 2.5]), True),
        (np.array([-1, 5]), False),
        (np.array([10, 3]), False),
    ],
)
def test_indicator_function_box_2d(box_2d_05, point, expected):
    is_in = box_2d_05.indicator_function(point)
    assert is_in == expected


# ================================
# ==== WRITE YOUR TESTS BELOW ====
# ================================


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[2.5, 2.5]]), np.array([2.5])),
        (np.array([[0, 5], [0, 5]]), np.array([2.5, 2.5])),
        (
            np.array([[0, 5], [-1, 3], [-10, 10]]),
            np.array([2.5, 1, 0]),
        ),
    ],
)
def test_box_center(bounds, expected):
    assert (BoxWindow(bounds).center() == expected).all()


@pytest.mark.parametrize(
    "args, expected",
    [
        ((10, np.array([[2.5, 2.5]])), np.array([[2.5, 2.5]])),
    ],
)
def test_unit_box_center(args, expected):
    assert (UnitBoxWindow(*args).center() == expected).all()


@pytest.mark.parametrize(
    "args, expected",
    [
        ((np.array([[2.5, 2.5]]), 10), np.array([[2.5, 2.5]])),
    ],
)
def test_center_ball_window(args, expected):
    assert (BallWindow(*args).center == expected).all()


@pytest.mark.parametrize(
    "args,  expected",
    [
        ((np.array([[2.5, 2.5]]), 10, np.array([[2.5, 2.5]])), True),
        ((np.array([[2, 5]]), 4, np.array([[2.5, 2.5]])), True),
        ((np.array([[2, 2]]), .5, np.array([[2.5, 2.5]])), False),
        ((np.array([[0, 2, 3]]), .5, np.array([[1, 2.5, 2.5]])), False),
        ((np.array([[0, 2, 3, 4]]), 5, np.array([[1, 3, 2.5, 2.5]])), True),
    ],
)
def test_in_ball_window(args, expected):
    assert BallWindow(*args[:2]).__contains__(args[-1]) == expected


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[2.5, 2.5]]), 1),
        (np.array([[0, 5], [0, 5]]), 2),
        (
            np.array([[0, 5], [-1.45, 3.14], [-10, 10]]),
            3,
        ),
    ],
)
def test__len__(bounds, expected):
    assert (BoxWindow(bounds).__len__()) == expected


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[2.5, 2.5]]), 1),
        (np.array([[0, 5], [0, 5]]), 2),
        (
            np.array([[0, 5], [-1.45, 3.14], [-10, 10]]),
            3,
        ),
    ],
)
def test_dimension(bounds, expected):
    assert (BoxWindow(bounds).dimension()) == expected


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[2.5, 2.5]]), 0),
        (np.array([[0, 5], [0, 5]]), 25),
        (
            np.array([[0, 5], [-1.45, 3.14], [-10, 10]]),
            459,
        ),
    ],
)
def test_volume(bounds, expected):
    assert (BoxWindow(bounds).volume() == expected)


@pytest.mark.parametrize(
    "bounds, n, expected",
    [
        (np.array([[2.5, 2.5]]), 2, True),
        (np.array([[0, 5], [0, 5]]), 4, True),
        (np.array([[0, 5], [-1.45, 3.14], [-10, 10]]), 8, True),
    ],
)
def test_rand_in_bounds(bounds, n, expected):
    a = BoxWindow(bounds)
    assert (all(elm in a for elm in a.rand(n, rng=1)) == expected)


# @pytest.mark.parametrize(
#     "bounds, n, expected",
#     [
#         (np.array([[2.5, 2.5]]), 2, np.array([[0.05910812], [2.25231848]])),
#         (np.array([[0, 5], [0, 5]]), 4,
#          np.array([[2.55910812, 4.75231848], [0.72079806, 4.74324724],
#                    [1.55915726, 2.11663224], [4.13851297, 2.04599568]])),
#         (np.array([[0, 5], [-1.45, 3.14], [-10, 10]
#                    ]), 1, np.array([[2.55910812, 2.91262837, -7.11680775]])),
#     ],
# )
# def test_rand_number(bounds, n, expected):
#     a = BoxWindow(bounds)
#     assert (a.rand(n, rng=1) == expected).all()
