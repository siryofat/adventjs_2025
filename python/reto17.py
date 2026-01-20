def has_four_lights(board: list[list[str]]) -> bool:
    rows = len(board)
    cols = len(board[0])

    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if col == ".":
                continue
            if c <= cols - 4:
                row_series = row[c : c + 4]
                if len(set(row_series)) == 1:
                    return True
            if r <= rows - 4:
                col_series = [s[c] for s in board[r : r + 4]]
                if len(set(col_series)) == 1:
                    return True
    return False
