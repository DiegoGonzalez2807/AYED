from sys import stdin

def mcd( a, b):
    while a > 0:
        a, b = b%a, a
    return b

def main():
    a , b = [ int(w) for w in stdin.readline().strip().split()]
    print(mcd(a,b))

main()