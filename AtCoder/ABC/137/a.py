import sys

def main():
    input = sys.stdin.readline
    a, b = map(int, input().split())
    return max(a+b, a-b, a*b)


if __name__ == '__main__':
    print(main())
