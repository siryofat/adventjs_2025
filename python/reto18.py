from collections.abc import Iterable


def has_four_in_a_row(board: list[list[str]]) -> bool:
    rows = len(board)
    cols = len(board[0]) if rows else 0
    series = 4

    def all_equal(cells: Iterable[str]) -> bool:
        cells = list(cells)
        return (
            len(cells) == series
            and cells[0] != "."
            and all(x == cells[0] for x in cells)
        )

    for r in range(rows):
        for c in range(cols):
            ch = board[r][c]
            if ch == ".":
                continue

            # Right
            if c + series <= cols and all_equal(board[r][c + k] for k in range(series)):
                return True

            # Down
            if r + series <= rows and all_equal(board[r + k][c] for k in range(series)):
                return True

            # Down-right
            if (
                r + series <= rows
                and c + series <= cols
                and all_equal(board[r + k][c + k] for k in range(series))
            ):
                return True

            # Down-left
            if (
                r + series <= rows
                and c - (series - 1) >= 0
                and all_equal(board[r + k][c - k] for k in range(series))
            ):
                return True

    return False
