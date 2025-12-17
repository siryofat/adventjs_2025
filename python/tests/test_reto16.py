import pytest

from reto16 import pack_gifts


@pytest.mark.parametrize(
    "gifts, max_weight, expected",
    [
        ([2, 3, 4, 1], 5, 2),
        ([3, 3, 2, 1], 3, 3),
        ([1, 1, 1, 1], 2, 2),
        ([5, 6, 1], 5, None),
        ([], 10, 0),
    ],
)
def test_pack_gifts(gifts, max_weight, expected):
    assert pack_gifts(gifts, max_weight) == expected
