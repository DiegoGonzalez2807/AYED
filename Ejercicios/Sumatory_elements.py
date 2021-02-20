def sumatory_elements(list_1,numbers):
    if numbers == 1:
        return list_1[0]
    else:
        return list_1[numbers-1] + sumatory_elements(list_1,numbers-1)
