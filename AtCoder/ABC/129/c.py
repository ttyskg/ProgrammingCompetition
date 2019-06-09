import sys

def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    is_safe = [True] * (N+1)
    for a in A:
        is_safe[a] = False

    dp = [0] * (N+2)
    dp[1] = 1
    for i in range(N):
        step = i+2
        if is_safe[i+1]:
            dp[step] = dp[step-1] + dp[step-2]
            dp[step] %= MOD
        else:
            dp[step] = 0

    return dp[N+1]


if __name__ == '__main__':
    print(main())
