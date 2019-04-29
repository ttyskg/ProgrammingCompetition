import sys

def main():
    input = sys.stdin.readline
    A, B, T = map(int, input().split())
    n = T // A
    return n * B


if __name__ == '__main__':
    print(main())
