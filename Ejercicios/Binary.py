def binary(number):
    if number > 1:
        binary(number//2)
    print(number%2, end = '')
