from reto15 import draw_table


def test_order_strings():
    input = [
        {"name": "Charlie", "city": "New York"},
        {"name": "Alice", "city": "London"},
        {"name": "Bob", "city": "Paris"},
    ]
    output = """+---------+----------+
| A       | B        |
+---------+----------+
| Alice   | London   |
| Bob     | Paris    |
| Charlie | New York |
+---------+----------+"""
    assert draw_table(input, "name") == output


def test_order_ints():
    input = [
        {"gift": "Book", "quantity": 5},
        {"gift": "Music CD", "quantity": 1},
        {"gift": "Doll", "quantity": 10},
    ]
    output = """+----------+----+
| A        | B  |
+----------+----+
| Music CD | 1  |
| Book     | 5  |
| Doll     | 10 |
+----------+----+"""
    assert draw_table(input, "quantity") == output


def test_empty_data():
    input = []
    assert draw_table(input, "") == ""
