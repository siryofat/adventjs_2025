from typing import Literal

board = """
.....
.*#.*
.@...
.....
"""

moves = ["DD", "U", "LL", "UUUUU", "RRRU", "RRRURR", "D", "R"]
#        crash, suc, cra, suc, suc, suc, fail, fail


def move_reno(board: str, moves: str) -> Literal["fail", "crash", "success"]:
    # Parse board
    lines = board.splitlines()
    rows = len(lines)
    cols = max((len(line) for line in lines), default=0)

    stars: set[tuple[int, int]] = set()
    obstacles: set[tuple[int, int]] = set()
    start: tuple[int, int] | None = None

    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch == "*":
                stars.add((r, c))
            elif ch == "#":
                obstacles.add((r, c))
            elif ch == "@":
                start = (r, c)

    if start is None:
        return "crash"  # no start found

    # Directions local to function
    DIRS: dict[str, tuple[int, int]] = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }

    r, c = start

    for mv in moves:
        dr, dc = DIRS[mv]
        nr, nc = r + dr, c + dc

        # Out of bounds (consider ragged lines)
        if not (0 <= nr < rows and 0 <= nc < len(lines[nr])):
            return "crash"

        next_pos = (nr, nc)

        # Obstacle check
        if next_pos in obstacles:
            return "crash"

        # Star check: success immediately regardless of what happens later
        if next_pos in stars:
            return "success"

        # Advance position
        r, c = nr, nc

    # No star collected and no crash after processing all moves
    return "fail"


for move in moves:
    print(move_reno(board, move))
