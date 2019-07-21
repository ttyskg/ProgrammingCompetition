import sys

def main():
    input = sys.stdin.readline
    N, D = map(int, input().split())
    return (N + 2*D) // (2*D + 1)


if __name__ == '__main__':
    print(main())
