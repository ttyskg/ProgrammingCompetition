import sys

def main():
    input = sys.stdin.readline
    l1, l2, l3 = map(int, input().split())

    if l1 == l2:
        return l3
    elif l2 == l3:
        return l1
    else:
        return l2

if __name__ == '__main__':
    print(main())
