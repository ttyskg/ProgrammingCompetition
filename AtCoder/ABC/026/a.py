import sys

def main():
    input = sys.stdin.readline
    A = int(input())
    x = A // 2
    y = A - x

    return x * y


if __name__ == '__main__':
    print(main())
