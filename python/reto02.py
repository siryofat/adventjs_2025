def manufacture_gifts(gifts_to_produce):
    gifts = []
    for gift in gifts_to_produce:
        quantity = gift["quantity"]
        if isinstance(quantity, int) and quantity > 0:
            gifts += [gift["toy"]] * quantity

    return gifts
