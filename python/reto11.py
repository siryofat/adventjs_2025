tests = [
    ([".*.", "*#*", ".*."], 0),
    (["...", ".*.", "..."], 1),
    (["*.*", "...", "*#*"], 2),
    ([".....", ".*.*.", "..#..", ".*.*.", "....."], 4),
]


def find_unsafe_gifts(warehouse: list[str]) -> int:
    gift = "*"
    cam = "#"
    rows = len(warehouse)
    cols = len(warehouse[0])
    unsafe = 0
    DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for r, row in enumerate(warehouse):
        for c, col in enumerate(row):
            if col == gift:
                cams = False
                for dir in DIRS:
                    dr, dc = dir
                    nr = r + dr
                    nc = c + dc
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        continue
                    if warehouse[nr][nc] == cam:
                        cams = True
                if not cams:
                    unsafe += 1
    return unsafe


for test in tests:
    input, expected = test
    res = find_unsafe_gifts(input)
    print(f"{res=}, {expected=}, {'ok' if res == expected else 'Fail'}")
