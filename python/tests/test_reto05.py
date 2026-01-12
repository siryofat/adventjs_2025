import pytest

from reto05 import time_until_take_off


@pytest.fixture
def take_off():
    return "2025*12*25@00|00|00 NP"


@pytest.mark.parametrize(
    "from_time, result",
    [
        ("2025*12*24@23|59|30 NP", 30),
        ("2025*12*25@00|00|00 NP", 0),
        ("2025*12*25@00|00|12 NP", -12),
    ],
)
def test_time_until_take_off(take_off, from_time, result):
    assert time_until_take_off(from_time, take_off) == result
