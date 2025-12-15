import pytest

from reto13 import run_factory


@pytest.mark.parametrize(
    "factory, expected",
    [
        ([">>."], "completed"),
        ([">>>"], "broken"),
        ([">><"], "loop"),
        ([">>v", "..<"], "completed"),
        ([">>v", "<<<"], "broken"),
        ([">v.", "^.."], "completed"),
        (["v.", "^."], "loop"),
    ],
)
def test_run_factory(factory, expected):
    output = run_factory(factory)
    assert output == expected
