import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))

    dp = [0 for _ in range(N)]
    dp[1] = abs(A[1] - A[0])
    for i in range(2, N):
        dp[i] = min(dp[i-2] + abs(A[i] - A[i-2]), dp[i-1] + abs(A[i] - A[i-1]))

    return dp[N-1]


if __name__ == '__main__':
    print(main())
