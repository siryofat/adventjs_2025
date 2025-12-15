def elf_battle(elf1: str, elf2: str) -> int:
    RULES = {
        "A": {"A": (1, 1), "B": (0, 0), "F": (2, 1)},
        "B": {"A": (0, 0), "B": (0, 0), "F": (2, 0)},
        "F": {"A": (1, 2), "B": (0, 2), "F": (2, 2)},
    }

    hp1 = 3
    hp2 = 3

    for atk1, atk2 in zip(elf1, elf2):
        dmg1, dmg2 = RULES[atk1][atk2]
        hp1 -= dmg1
        hp2 -= dmg2
        if hp1 <= 0 and hp2 <= 0:
            return 0
        elif hp1 <= 0:
            return 2
        elif hp2 <= 0:
            return 1

    if hp1 == hp2:
        return 0
    elif hp1 < hp2:
        return 2
    else:
        return 1
