import sys

def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    MOD = 10**9 + 7

    ans = 0
    for i in range(N*M - K + 1):
        r = i // M
        c = i % M

        row_dist = c * (c + 1) // 2 + (M - c) * (M - c + 1) // 2
        s = row_dist * (N - r) + (N - r) * (N - r + 1) // 2 - c * (c + 1) // 2
        ans += s * (K-1)
        ans %= MOD

    return ans


if __name__ == '__main__':
    print(main())
