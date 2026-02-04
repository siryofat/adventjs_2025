import pytest
from reto19 import reveal_santa_route


@pytest.mark.parametrize(
    "routes, expected",
    [
        ([["MEX", "CAN"], ["UK", "GER"], ["CAN", "UK"]], ["MEX", "CAN", "UK", "GER"]),
        (
            [
                ["USA", "BRA"],
                ["JPN", "PHL"],
                ["BRA", "UAE"],
                ["UAE", "JPN"],
                ["CMX", "HKN"],
            ],
            ["USA", "BRA", "UAE", "JPN", "PHL"],
        ),
        ([["STA", "HYD"], ["ESP", "CHN"]], ["STA", "HYD"]),
    ],
)
def test_reveal_santa_route(routes: list[list[str]], expected: list[str]):
    assert reveal_santa_route(routes) == expected
