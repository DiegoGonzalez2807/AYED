def MCDrecur(a,b):
    if b == 0:
        return a
    return MCDrecur(b,a%b)