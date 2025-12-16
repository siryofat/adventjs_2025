import string


def draw_table(data: list[dict[str, str | int]], sortBy: str) -> str:
    ordered = sorted(data, key=lambda s: s[sortBy])
    cols = string.ascii_uppercase[: len((data[0]))]
    pads = [max(len(str(r.get(k, ""))) for r in data) for k in data[0].keys()]

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
