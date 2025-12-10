from typing import Literal

board = """
.....
.*#.*
.@...
.....
"""

moves = "DD"


def move_reno(board: str, moves: str) -> Literal["fail", "crash", "success"]:
    row: int = -1
    col: int = 0
    rows: int = 0
    cols: int = 0
    stars: set[tuple[int, int]] = set()
    obstacles: set[tuple[int, int]] = set()
    start: tuple[int, int] = (0, 0)

    for char in board:
        pos = (row, col)
        if char == "*":
            stars.add(pos)
        elif char == "#":
            obstacles.add(pos)
        elif char == "@":
            start = pos
        elif char == "\n":
            cols = col if col > cols else cols
            col = 0
            row += 1
            continue
        col += 1

    rows = row
    print(f"{rows=}, {cols=}, {stars=}, {obstacles=}, {start=}")

    DIRS = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }

    pos: tuple[int, int] = start
    success: bool = False
    for move in moves:
        r, c = pos
        dr, dc = DIRS[move]
        nr, nc = r + dr, c + dc
        next_pos: tuple[int, int] = (nr, nc)
        if not (0 <= nr < rows and 0 <= nc < cols):
            return "success" if success else "crash"
        elif next_pos in stars:
            success = True
        elif next_pos in obstacles:
            return "crash"
        pos = next_pos
        print(next_pos)

    return "success" if success else "fail"


print(board)
print(moves)
move_reno(board, moves)
print(move_reno(board, moves))
