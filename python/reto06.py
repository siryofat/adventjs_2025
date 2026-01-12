def match_gloves(gloves: list[dict[str, str]]) -> list[str]:
    unmatched: dict[str, set[str]] = {}
    result: list[str] = []

    for g in gloves:
        color = g["color"]
        hand = g["hand"]
        opp = "R" if hand == "L" else "L"

        s = unmatched.setdefault(color, set())
        if opp in s:
            s.remove(opp)
            result.append(color)  # pair formed now, preserves order
        else:
            s.add(hand)

    return result
