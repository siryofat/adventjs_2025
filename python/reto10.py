def max_depth(s: str) -> int:
    depth = 0
    max_depth = 0
    for char in s:
        if char == "[":
            depth += 1
        else:
            max_depth = max(max_depth, depth)
            depth -= 1
            if depth < 0:
                return -1
    return max_depth if depth == 0 else -1
