import sys
import numpy as np

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dp = np.zeros(N+1, dtype=np.int)
    for i in range(3):
        a = A[i]
        n = N // a
        for k in range(1, n+1):
            dp[k*a:] = np.maximum(dp[k*a:], dp[:N-k*a+1] + k*B[i])

    M = dp[N]
    dp = np.zeros(M+1, dtype=np.int)
    for i in range(3):
        a = B[i]
        n = M // a
        for k in range(1, n+1):
            dp[k*a:] = np.maximum(dp[k*a:], dp[:M-k*a+1] + k*A[i])

    return dp[M]


if __name__ == '__main__':
    print(main())
