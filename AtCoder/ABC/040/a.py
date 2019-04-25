import sys

def main():
    input = sys.stdin.readline
    n, x = map(int, input().split())
    return min(x-1, n-x)


if __name__ == '__main__':
    print(main())
