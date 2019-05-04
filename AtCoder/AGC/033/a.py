#ref: https://atcoder.jp/contests/agc033/submissions/5260580

import sys
import numpy as np

def main():
    input = sys.stdin.readline
    H, W = map(int, input().split())
    INF = H * W
    dp = [[INF if c == '.' else 0 for c in input().strip()] for _ in range(H)]
    dp = np.array(dp)

    for i in range(1, H):
        dp[i, :] = np.minimum(dp[i, :], dp[i-1, :] + 1)

    for i in range(H-2, -1, -1):
        dp[i, :] = np.minimum(dp[i, :], dp[i+1, :] + 1)

    for i in range(1, W):
        dp[:, i] = np.minimum(dp[:, i], dp[:, i-1] + 1)

    for i in range(W-2, -1, -1):
        dp[:, i] = np.minimum(dp[:, i], dp[:, i+1] + 1)

    return np.max(dp)

if __name__ == '__main__':
    print(main())
