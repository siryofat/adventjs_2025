def filter_gifts(gifts):
    # Code here
    good = []
    for gift in gifts:
        if "#" in gift:
            continue
        good.append(gift)
    return good
