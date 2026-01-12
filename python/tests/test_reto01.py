import pytest

from reto01 import filter_gifts


@pytest.mark.parametrize(
    "gifts, expected",
    [
        (["car", "doll#arm", "ball", "#train"], ["car", "ball"]),
        (["#broken", "#rusty"], []),
        ([], []),
    ],
)
def test_filter_gifts(gifts, expected):
    assert filter_gifts(gifts) == expected
