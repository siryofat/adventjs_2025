def clear_gifts(warehouse: list[list[str]], drops: list[int]) -> list[list[str]]:
    local = [row.copy() for row in warehouse]

    rows = len(local)
    cols = len(local[0])

    for drop in drops:
        for r in range(rows - 1, -1, -1):
            if local[r][drop] == ".":
                local[r][drop] = "#"
                row = local[r]
                if len(set(row)) == 1:
                    local.pop(r)
                    local.insert(0, ["."] * cols)
                break

    return local
