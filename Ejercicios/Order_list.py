def order_list(list_1):
    if len(list_1) <= 1:
        return list_1[:]
    min_value = min(list_1)
    list_1.remove(min_value)
    return [min_value] + order_list(list_1[:])
