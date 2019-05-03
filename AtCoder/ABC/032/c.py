import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    S = [int(input()) for _ in range(N)]

    if 0 in S:
        return N

    if K == 0:
        return 0

    l, r = 0, 0
    ans = 0
    m = 1
    while r < N:
        while r < N and m <= K:
            ans = max(ans, r-l)
            m *= S[r]
            r += 1

        while l < r and m > K:
            m //= S[l]
            l += 1

    ans = max(ans, r-l)
    return ans


if __name__ == '__main__':
    print(main())
