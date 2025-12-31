import pytest

from reto20 import clear_gifts


@pytest.mark.parametrize(
    "warehouse, drops, expected",
    [
        (
            [[".", ".", "."], [".", ".", "."], ["#", ".", "#"]],
            [1],
            [[".", ".", "."], [".", ".", "."], [".", ".", "."]],
        ),
        (
            [[".", ".", "#"], ["#", ".", "#"], ["#", ".", "#"]],
            [0, 1, 2],
            [[".", ".", "#"], ["#", ".", "#"], ["#", ".", "#"]],
        ),
    ],
)
def test_drop_gifts(warehouse, drops, expected):
    assert clear_gifts(warehouse, drops) == expected
