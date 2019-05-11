import sys

def main():
    input = sys.stdin.readline
    A, B = map(str, input().split())
    N = int(A + B)

    return N * 2


if __name__ == '__main__':
    print(main())
