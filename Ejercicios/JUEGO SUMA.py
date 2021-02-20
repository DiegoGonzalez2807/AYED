from sys import stdin
def ways(n,array,leng,dictio,i):
    if i > leng - 1:
        return 0
    else:
        if n - array[i] == 0:
            return 1
        elif n - array[i] < 0:
            return 0
        else:
            return ways(n-array[i],array,leng,dictio,i) + ways(n,array,leng,dictio,i+1)
def memory(n,array,leng,dictio,i):
    if (n,array[i]) in dictio.keys():
        return dictio((n,array[i]))
    else:
        dictio[(n,i)] = ways(n,array,leng,dictio,i)
    return dictio[(n,i)]
def main():
    line = list(map(int,stdin.readline().strip().split()))
    expected = line[0]
    leng = line[1]
    array = line[2:len(line)]
    dictio = {}
    while line:
        print('Sums of', expected, ':')
        print(memory(expected,array,leng,dictio,0))
        line = list(map(int, stdin.readline().strip().split()))
        expected = line[0]
        leng = line[1]
        array = line[2:len(line)]

main()