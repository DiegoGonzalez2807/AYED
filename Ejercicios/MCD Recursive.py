from sys import stdin
def MCD(first_element,last_element):
    if last_element == 0:
        return first_element
    else:
        return MCD(last_element,first_element%last_element)

def main():
    numbers = stdin.readline().strip().split()
    a, b = int(numbers[0]), int(numbers[1])
    print(MCD(a,b))
