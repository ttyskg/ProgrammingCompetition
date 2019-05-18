import numpy as np
import sys

def main():
    input = sys.stdin.readline
    W = int(input())
    N, K = map(int, input().split())
    screenshots = [tuple(map(int, input().split())) for _ in range(N)]

    dp = np.full((K+1, W+1), -float('inf'))
    dp[0, 0] = 0
    for w, v in screenshots:
        if w > W:
            continue

        dp[1:, w:] = np.maximum(dp[1:, w:], dp[:K, :W+1-w] + v)

    return int(np.max(dp))


if __name__ == '__main__':
    print(main())
