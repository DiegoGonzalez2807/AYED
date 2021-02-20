from sys import stdin
def ways_1(expected,long_array,arrays,i):
    if i < long_array:
        if arrays[i] == expected:
            return 1
        if arrays[i] > expected:
            return 0
        if arrays[i] < expected and i+1 == long_array:
            return 0
        if arrays[i] < expected:
            print(expected-arrays[i],long_array,arrays,i+1)
            print(expected,long_array,arrays,i+1)
            return ways_1(expected-arrays[i],long_array,arrays,i+1) + ways_1(expected,long_array,arrays,i+1)


def main():
    line = list(map(int,stdin.readline().strip().split()))
    expected, long_array, arrays = line[0], line[1], line[2:len(line)]
    print(line,expected, long_array, arrays)
    while expected and long_array != 0:
        print(ways_1(expected,long_array,arrays,0))
        line = list(map(int, stdin.readline().strip().split()))
        expected, long_array, arrays = line[0], line[1], line[2:len(line)]
        print(line, expected, long_array, arrays)


main()
