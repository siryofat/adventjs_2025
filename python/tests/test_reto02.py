import pytest

from reto02 import manufacture_gifts

production1 = [
    {"toy": "car", "quantity": 3},
    {"toy": "doll", "quantity": 1},
    {"toy": "ball", "quantity": 2},
]

result1 = ["car", "car", "car", "doll", "ball", "ball"]

production2 = [
    {"toy": "train", "quantity": 0},
    {"toy": "bear", "quantity": -2},
    {"toy": "puzzle", "quantity": 1},
]
result2 = ["puzzle"]


@pytest.mark.parametrize(
    "production, result", [(production1, result1), (production2, result2), ([], [])]
)
def test_manufacture_gifts(production, result):
    assert manufacture_gifts(production) == result
