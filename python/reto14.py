from collections import deque

workshop = {
    "storage": {"shelf": {"box1": "train", "box2": "switch"}, "box": "car"},
    "gift": "doll",
}

tests = [
    (workshop, "train", ["storage", "shelf", "box1"]),
    (workshop, "switch", ["storage", "shelf", "box2"]),
    (workshop, "car", ["storage", "box"]),
    (workshop, "doll", ["gift"]),
    (workshop, "plane", []),
]


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


for test in tests:
    ws, gift, expected = test
    output = find_gift_path(ws, gift)
    print(f"{output=}, {expected=}, {'ok' if output == expected else '<-------FAIL'}")
