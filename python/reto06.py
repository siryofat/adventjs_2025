from collections import defaultdict
from typing import Dict, List

sample_data = [
    [
        {"hand": "L", "color": "red"},
        {"hand": "R", "color": "red"},
        {"hand": "R", "color": "green"},
        {"hand": "L", "color": "blue"},
        {"hand": "L", "color": "green"},
    ],
    [
        {"hand": "L", "color": "gold"},
        {"hand": "R", "color": "gold"},
        {"hand": "L", "color": "gold"},
        {"hand": "L", "color": "gold"},
        {"hand": "R", "color": "gold"},
    ],
    [
        {"hand": "L", "color": "red"},
        {"hand": "R", "color": "green"},
        {"hand": "L", "color": "blue"},
    ],
]


def match_gloves(gloves: List[Dict[str, str]]) -> List[str]:
    ordered = defaultdict(list)
    valids = []
    for glove in gloves:
        hand, color = glove.values()
        if hand == "L":
            if color in ordered["R"]:
                ordered["R"].remove(color)
                valids.append(color)
            else:
                ordered["L"].append(color)
        else:
            if color in ordered["L"]:
                ordered["L"].remove(color)
                valids.append(color)
            else:
                ordered["R"].append(color)

    return valids


for sample in sample_data:
    print(match_gloves(sample))
