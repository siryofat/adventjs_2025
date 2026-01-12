def decode_santa_pin(code: str) -> str | None:
    import re
    from collections import Counter

    found = re.findall(re.compile(r"\[(.*?)\]"), code)
    if len(found) < 4:
        return None
    out = ""
    for group in found:
        if len(group) == 1:
            char = group[0]
            if char == "<":
                out += out[-1]
                continue
            else:
                out += char
                continue
        number = group[0]
        operations = Counter(group[1:])
        new = (
            int(number) + operations.get("+", 0) * 1 - operations.get("-", 0) * 1
        ) % 10
        out += str(new)
    return out
