import sys

def main():
    input = sys.stdin.readline
    A, B = map(int, input().split())
    return (B + A - 1) // A


if __name__ == '__main__':
    print(main())
