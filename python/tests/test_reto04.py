import pytest

from reto04 import decode_santa_pin


@pytest.mark.parametrize(
    "code, result",
    [("[1++][2-][3+][<]", "3144"), ("[9+][0-][4][<]", "0944"), ("[1+][2-]", None)],
)
def test_decode_santa_pin(code, result):
    assert decode_santa_pin(code) == result
