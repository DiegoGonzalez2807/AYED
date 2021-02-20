from sys import stdin
def sum_pairs(element):
    if element % 2 == 1:
        element -=1
    if element == 0:
        return 0
    else:
        return element  + sum_pairs(element-2)

def main():
    number = int(stdin.readline().strip())
    print(sum_pairs(number))