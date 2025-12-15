import pytest

from reto09 import move_reno


@pytest.fixture
def board():
    return """
.....
.*#.*
.@...
.....
"""


@pytest.mark.parametrize(
    "moves, expected",
    [
        ("D", "fail"),
        ("U", "success"),
        ("RU", "crash"),
        ("RRRUU", "success"),
        ("DD", "crash"),
        ("UUU", "success"),
        ("RR", "fail"),
        ("LL", "crash"),
    ],
)
def test_move_reno(board, moves, expected):
    output = move_reno(board, moves)
    assert output == expected
