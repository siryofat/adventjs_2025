import pytest

from reto10 import max_depth


@pytest.mark.parametrize(
    "s, expected",
    [
        (("[]"), 1),
        (("[[]]"), 2),
        (("[][]"), 1),
        (("[[][]]"), 2),
        (("[[[]]]"), 3),
        (("[][[]][]"), 2),
        (("]["), -1),  # (cierra antes de abrir)
        (("[[["), -1),  # (faltan cierres)
        (("[]]]"), -1),  # (sobran cierres)
        (("[][]["), -1),  # (queda uno sin cerrar)
    ],
)
def test_max_depth(s, expected):
    output = max_depth(s)
    assert output == expected
