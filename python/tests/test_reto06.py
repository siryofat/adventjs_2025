import pytest

from reto06 import match_gloves

sample_data = [
    [
        {"hand": "L", "color": "red"},
        {"hand": "R", "color": "red"},
        {"hand": "R", "color": "green"},
        {"hand": "L", "color": "blue"},
        {"hand": "L", "color": "green"},
    ],
    [
        {"hand": "L", "color": "gold"},
        {"hand": "R", "color": "gold"},
        {"hand": "L", "color": "gold"},
        {"hand": "L", "color": "gold"},
        {"hand": "R", "color": "gold"},
    ],
    [
        {"hand": "L", "color": "red"},
        {"hand": "R", "color": "green"},
        {"hand": "L", "color": "blue"},
    ],
    [
        {"hand": "L", "color": "green"},
        {"hand": "L", "color": "red"},
        {"hand": "R", "color": "red"},
        {"hand": "R", "color": "green"},
    ],
]

results = [["red", "green"], ["gold", "gold"], [], ["red", "green"]]


@pytest.mark.parametrize("input_gloves,expected", list(zip(sample_data, results)))
def test_match_gloves(input_gloves, expected):
    assert match_gloves(input_gloves) == expected
