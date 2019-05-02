import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    if n % 2 == 1:
        return n+1
    else:
        return n-1


if __name__ == '__main__':
    print(main())
