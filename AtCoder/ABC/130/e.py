import sys

def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    N, M = map(int, input().split())
    S = [0] + list(map(int, input().split()))
    T = [0] + list(map(int, input().split()))

    dp = [[0] * (M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
            if S[i] == T[j]:
                dp[i][j] += dp[i-1][j-1] + 1
            dp[i][j] %= MOD

    return (dp[N][M] + 1) % MOD


if __name__ == '__main__':
    print(main())
