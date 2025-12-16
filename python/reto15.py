import string


def draw_table(data: list[dict[str, str | int]], sortBy: str) -> str:
    if not data:
        return ""

    ordered = sorted(data, key=lambda s: s[sortBy])
    first_keys = list(data[0].keys())
    all_keys = set(first_keys)
    for row in data[1:]:
        all_keys.update(row.keys())
    extra_keys = sorted(k for k in all_keys if k not in first_keys)
    columns = first_keys + extra_keys

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
