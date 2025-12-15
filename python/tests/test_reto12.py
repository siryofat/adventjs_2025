import pytest

from reto12 import elf_battle


@pytest.mark.parametrize(
    "elf1, elf2, expected",
    [
        ("A", "B", 0),
        ("F", "B", 1),
        ("AAB", "BBA", 0),
        ("AFA", "BBA", 1),
        ("AFAB", "BBAF", 1),
        ("AA", "FF", 2),
    ],
)
def test_elf_battle(elf1, elf2, expected):
    output = elf_battle(elf1, elf2)
    assert output == expected
