import sys

def main():
    input = sys.stdin.readline
    L, H = map(int, input().split())
    N = int(input())
    for _ in range(N):
        A = int(input())
        if L <= A <= H:
            print(0)
        elif A < L:
            print(L - A)
        else:
            print(-1)


if __name__ == '__main__':
    main()
