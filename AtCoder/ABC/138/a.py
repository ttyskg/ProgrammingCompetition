import sys

def main():
    input = sys.stdin.readline
    A = int(input())
    S = str(input().strip())
    if A >= 3200:
        return S
    else:
        return 'red'


if __name__ == '__main__':
    print(main())
