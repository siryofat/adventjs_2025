import pytest

from reto14 import find_gift_path


@pytest.fixture
def workshop():
    return {
        "storage": {"shelf": {"box1": "train", "box2": "switch"}, "box": "car"},
        "gift": "doll",
    }


@pytest.mark.parametrize(
    "gift, expected",
    [
        ("train", ["storage", "shelf", "box1"]),
        ("switch", ["storage", "shelf", "box2"]),
        ("car", ["storage", "box"]),
        ("doll", ["gift"]),
        ("plane", []),
    ],
)
def test_find_gift_path(workshop, gift, expected):
    output = find_gift_path(workshop, gift)
    assert output == expected
