from collections import Counter


def find_unique_toy(toy: str) -> str:
    low = toy.lower()
    letters = Counter(low)
    uniques: list[int] = []
    for char, count in letters.items():
        if count == 1:
            uniques.append(low.index(char))
    if uniques:
        first = min(uniques)
        return toy[first]
    return ""
