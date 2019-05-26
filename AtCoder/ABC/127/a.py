import sys

def main():
    input = sys.stdin.readline
    A, B = map(int, input().split())

    if A <= 5:
        return 0
    elif 6 <= A <=12:
        return B // 2
    else:
        return B

if __name__ == '__main__':
    print(main())
