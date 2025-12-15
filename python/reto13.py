tests = [
    ([">>."], "completed"),
    ([">>>"], "broken"),
    ([">><"], "loop"),
    ([">>v", "..<"], "completed"),
    ([">>v", "<<<"], "broken"),
    ([">v.", "^.."], "completed"),
    (["v.", "^."], "loop"),
]


def run_factory(factory: list[str]) -> str:
    rows = len(factory)
    cols = len(factory[0])

    MOV = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}

    r = 0
    c = 0

    seen = set()
    while True:
        if (r, c) in seen:
            return "loop"
        else:
            seen.add((r, c))

        pos = factory[r][c]
        if pos == ".":
            return "completed"

        dr, dc = MOV[pos]
        r += dr
        c += dc
        if not (0 <= r < rows and 0 <= c < cols):
            return "broken"
