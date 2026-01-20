import pytest
from reto17 import has_four_lights


@pytest.mark.parametrize(
    "board, expected",
    [
        (
            [
                [".", ".", ".", ".", "."],
                ["R", "R", "R", "R", "."],
                ["G", "G", ".", ".", "."],
            ],
            True,
        ),
        ([[".", "G", ".", "."]] * 4, True),
        ([["R", "G", "R"], ["G", "R", "G"], ["G", "R", "G"]], False),
        ([["R", "R", "R", "."], ["."] * 4], False),
        ([[".", ".", "R", "R", "R", "R"], ["."] * 6], True),
        ([["."] * 4] * 2, False),
        ([["G"] * 5], True),
        ([["R", ".", "."]] * 4, True),
    ],
)
def test_advent_js(board: list[list[str]], expected: str):
    assert has_four_lights(board) == expected
