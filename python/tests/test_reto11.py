import pytest

from reto11 import find_unsafe_gifts


@pytest.mark.parametrize(
    "warehouse, expected",
    [
        ([".*.", "*#*", ".*."], 0),
        (["...", ".*.", "..."], 1),
        (["*.*", "...", "*#*"], 2),
        ([".....", ".*.*.", "..#..", ".*.*.", "....."], 4),
    ],
)
def test_find_unsafe_gifts(warehouse, expected):
    output = find_unsafe_gifts(warehouse)
    assert output == expected
