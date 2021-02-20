def pairs(N,current):
    if current > N:
        return 0
    return current + pairs(N,current+2)