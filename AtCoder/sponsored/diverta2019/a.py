import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())

    return N - K + 1


if __name__ == '__main__':
    print(main())
