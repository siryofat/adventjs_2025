def reveal_santa_route(routes: list[list[str]]) -> list[str]:
    tree: dict[str, str] = {k: v for k, v in routes}

    start: str = routes[0][0]
    pos: str = start

    route: list[str] = [start]

    while True:
        nxt: str | None = tree.get(pos)
        if nxt is None:
            return route
        route.append(nxt)
        pos = nxt
