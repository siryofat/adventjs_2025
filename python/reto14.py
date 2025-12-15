from collections import deque


def find_gift_path(workshop: dict, gift: str | int | bool) -> list[str]:
    q = deque()
    q.append(([], workshop))

    while q:
        path, node = q.popleft()

        if isinstance(node, dict):
            for key, value in node.items():
                q.append(([*path, key], value))

        if node == gift:
            return path

    return []
