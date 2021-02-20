def invert_list(list_1):
    if len(list_1) == 0:
        return list_1
    else:
        last_list = [list_1[-1]]
        return last_list + invert_list(list_1[:-1])