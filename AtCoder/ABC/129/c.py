import sys

def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    is_safe = [True] * (N+2)
    for a in A:
        is_safe[a+1] = False

    dp = [0] * (N+2)
    dp[1] = 1
    for i in range(2, N+2):
        if is_safe[i]:
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] %= MOD
        else:
            dp[i] = 0

    return dp[N+1]


if __name__ == '__main__':
    print(main())
