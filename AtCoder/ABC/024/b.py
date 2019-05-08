import sys

def main():
    input = sys.stdin.readline
    N, T = map(int, input().split())
    A = [int(input()) for _ in range(N)]

    ans = 0
    t = A[0]
    for a in A:
        ans += min(a - t, T)
        t = a
    ans += T

    return ans


if __name__ == '__main__':
    print(main())
