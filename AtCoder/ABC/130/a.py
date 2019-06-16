import sys

def main():
    input = sys.stdin.readline
    X, A = map(int, input().split())

    if X < A:
        return 0
    else:
        return 10

if __name__ == '__main__':
    print(main())
