from sys import stdin
def perfect(number):
    list_1 = list(map(int,number))
    suma = sum(list_1)
    if len(list_1) == 1:
        return int(list_1[0])
    else:

        return perfect(str(suma))
def main():
    line = stdin.readline().strip().split()
    while len(line) != 0:
        a, b = int(line[0]), str(line[1])
        number_perfect = a * b
        print(perfect(number_perfect))
        line = stdin.readline().strip().split()
main()