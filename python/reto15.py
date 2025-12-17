import string


def draw_table(data: list[dict[str, str | int]], sortBy: str) -> str:
    if not data:
        return ""

    ordered = sorted(data, key=lambda s: s[sortBy])

    columns = []
    seen = set()
    for row in data:
        for k in row.keys():
            if k not in seen:
                seen.add(k)
                columns.append(k)

    pads = [max(len(str(r.get(k, ""))) for r in data) for k in columns]
    cols = string.ascii_uppercase[: len(columns)]

    hline = "".join(["+", *["-" * (n + 2) + "+" for n in pads]])
    header = "".join(["|", *[f" {c.ljust(pads[i])} |" for i, c in enumerate(cols)]])
    body = []

    for item in ordered:
        body.append(
            "".join(
                [
                    "|",
                    *[
                        f" {str(v).ljust(pads[i])} |"
                        for i, v in enumerate(item.values())
                    ],
                ]
            )
        )

    table = [hline, header, hline, *body, hline]

    return "\n".join(table)
