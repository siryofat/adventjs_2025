from collections import deque


def can_escape(maze: list[list[str]]) -> bool:
    moves = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    rows = len(maze)
    cols = len(maze[0])
    q = deque()
    for r, row in enumerate(maze):
        for c, col in enumerate(row):
            if col == "S":
                q.append((r, c))
                break
    return False
