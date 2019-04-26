import sys

def main():
    input = sys.stdin.readline
    A = list(map(int, input().split()))
    return (A[0] * A[1]) * 2 + (A[1] * A[2]) * 2 + (A[2] * A[0]) * 2


if __name__ == '__main__':
    print(main())
