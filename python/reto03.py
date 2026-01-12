def draw_gift(size: int, symbol: str) -> str:
    if size <= 1:
        return ""
    ends: str = symbol * size
    if size == 2:
        return "\n".join([ends] * 2)
    mids: str = symbol + " " * (size - 2) + symbol
    wrap: list[str] = [ends] + [mids] * (size - 2) + [ends]
    return "\n".join(wrap)
