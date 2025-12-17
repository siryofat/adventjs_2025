def pack_gifts(gifts: list[int], max_weight: int) -> int | None:
    if not gifts:
        return 0

    total = 0
    weight = 0

    for gift in gifts:
        if gift > max_weight:
            return None

        new_weight = weight + gift
        if new_weight >= max_weight:
            total += 1
            weight = 0 if new_weight == max_weight else gift
        else:
            weight = new_weight

    if weight:
        total += 1

    return total
