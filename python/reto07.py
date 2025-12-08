input = [
    [5, "o", 2],
    [3, "@", 3],
    [4, "+", 1],
]


def draw_tree(height, ornament, frequency):
    width = 1 + (2 * (height - 1))
    mid = width // 2
    lines = []
    pos = 1
    for i in range(1, height + 1):
        line_width = 1 + (2 * (i - 1))
        empty = (width - line_width) // 2
        ends = " " * empty
        tree = []
        for p in range(pos, pos + line_width):
            char = "*" if p % frequency != 0 else ornament
            tree.append(char)
        tree_str = "".join(tree)
        pos += line_width
        lines.append(ends + tree_str)
    last_line = " " * (mid) + "#"
    lines.append(last_line)

    return "\n".join(lines)


for test in input:
    print(draw_tree(*test))
