import pytest
from reto08 import find_unique_toy


@pytest.mark.parametrize(
    "input, output",
    [
        ("Gift", "G"),
        ("sS", ""),
        ("reindeeR", "i"),
        ("AaBbCc", ""),
        ("abcDEF", "a"),
        ("aAaAaAF", "F"),
        ("sTreSS", "T"),
        ("z", "z"),
    ],
)
def test_find_unique_toy(input: str, output: str):
    assert find_unique_toy(input) == output
