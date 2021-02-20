from sys import stdin
def ways_1(expected,memory,i,array1):
    for i in range(len(memory)):
        if i < len(memory):
            if memory[i] == expected:
                return 1
            if memory[i] > expected:
                return 0
            print(expected-memory[i],memory,i+1,array1 + [expected-memory[i]])
            print(expected,memory,i+1, array1 + [expected])
            return ways_1(expected-memory[i],memory,i+1,array1 + [expected-memory[i]]) + ways_1(expected,memory,i+1, array1 + [expected])
"""Error de identacion en ways_1, falta una parte del codigo en el primer for"""

def main():
    line = int(stdin.readline().strip())
    memory = [1,5,10,25,50]
    while line != '':
        print(ways_1(line,memory,0,[]))
        line = int(stdin.readline().strip())




main()
