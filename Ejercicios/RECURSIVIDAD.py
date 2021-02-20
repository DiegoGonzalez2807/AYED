from sys import stdin
def invert_sort(list):
    return[max(list)] + invert_sort(list[:list.index(max(list))] + list[list.index(max(list))-1]) if len(list) > 1 else list[:]
def main():
    print(invert_sort([1,7,4,32,6,3,2,5,7]))
main()