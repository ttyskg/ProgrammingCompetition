import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())

    if K == 1:
        return 0
    else:
        return N - K

if __name__ == '__main__':
    print(main())
