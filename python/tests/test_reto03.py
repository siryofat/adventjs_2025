import pytest

from reto03 import draw_gift


@pytest.mark.parametrize(
    "size, symbol, result",
    [
        (4, "*", "****\n*  *\n*  *\n****"),
        (3, "#", "###\n# #\n###"),
        (2, "-", "--\n--"),
        (1, "+", ""),
    ],
)
def test_draw_gift(size, symbol, result):
    assert draw_gift(size, symbol) == result
