import sys

def main():
    input = sys.stdin.readline
    A, P = map(int, input().split())

    return (3*A + P) // 2


if __name__ == '__main__':
    print(main())
