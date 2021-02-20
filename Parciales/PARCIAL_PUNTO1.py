#Diego Alejandro Gonzalez Gualteros
#2163199
#C.C. 1007196603
#PUNTO1 POWER SUM
from sys import stdin
def power_sum(expected,num2,ind_base):
    proof_1 = ind_base ** num2
    if expected == proof_1:
        return 1
    if expected < proof_1:
        return 0
    else:
        return power_sum(expected-proof_1, num2, ind_base+1) + power_sum(expected, num2, ind_base+1)
def main():
    line = list(map(int,stdin.readline().strip().split()))
    line2 = list(map(int,stdin.readline().strip().split()))
    while len(line) != 0 or len(line2) != 0:
        answer = power_sum(line[0],line2[0], 1)
        print(answer)
        line = list(map(int, stdin.readline().strip().split()))
        line2 = list(map(int, stdin.readline().strip().split()))
main()