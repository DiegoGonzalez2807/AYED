def order(list):
    if len(list) <= 1:
        return list[:]
    minimum = min(list)
    list.remove(minimum)
    return [minimum] + order(list[:])