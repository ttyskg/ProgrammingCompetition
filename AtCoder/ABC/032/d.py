import numpy as np
import sys
from collections import defaultdict


def case1(N, W):
    d = defaultdict(lambda: 0)
    d[0] = 0
    ans = 0
    for _ in range(N):
        v, w = map(int, input().split())
        if w > W:
            continue

        d_ = defaultdict(lambda: 0)
        for w0, v0 in d.items():
            d_[w0] = max(d_[w0], v0)
            ans = max(ans, d_[w0])

            w1 = w + w0
            if w1 <= W:
                d_[w1] = max(d_[w1], v0 + v)
                ans = max(ans, d_[w1])
        d = d_
    return ans


def case2(N, W, items):
    dp = np.full((N+1, W+1), -np.inf)
    dp[0, 0] = 0
    for i, (v, w) in enumerate(items, start=1):
        dp[i] = dp[i-1]
        if w <= W:
            dp[i, w:] = np.maximum(dp[i][w:], dp[i-1][:W-w+1] + v)

    return int(np.max(dp[N]))


def case3(N, W, V, items):
    dp = np.full((N+1, V+1), np.inf)
    dp[0, 0] = 0
    for i, (v, w) in enumerate(items, start=1):
        dp[i] = dp[i-1]
        dp[i, v:] = np.minimum(dp[i, v:], dp[i-1][:V-v+1] + w)

    for i in range(V, -1, -1):
        if dp[N][i] <= W:
            return i


def main():
    input = sys.stdin.readline
    N, W = map(int, input().split())

    if N <= 30:
        return case1(N, W)

    max_w = 0
    sum_v = 0
    items = []
    for _ in range(N):
        v, w = map(int, input().split())
        items.append((v, w))
        max_w = max(max_w, w)
        sum_v += v

    if max_w <= 1000:
        return case2(N, W, items)

    else:  # max value is less than or equal 1000.
        return case3(N, W, sum_v, items)


if __name__ == '__main__':
    print(main())
