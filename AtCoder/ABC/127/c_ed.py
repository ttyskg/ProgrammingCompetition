import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    L = 0
    R = 10**5 + 1
    for _ in range(M):
        left, right = map(int, input().split())
        L = max(L, left)
        R = min(R, right)

    return max(R - L + 1, 0)


if __name__ == '__main__':
    print(main())
