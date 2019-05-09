#ref: https://atcoder.jp/contests/abc023/submissions/4467435

import numpy as np
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    A = [tuple(map(int, input().split())) for _ in range(N)]
    balloon = np.array(A)
    h = balloon[:, 0]
    s = balloon[:, 1]

    l = h.min()
    r = h.max() + s.max() * N
    checker = np.arange(N)
    while l != r:
        estimate = (l + r) // 2  # Estimated maximum reach of the balloons.
        t = (estimate - h) // s  # Time to reach the estimated hight.

        # Check if all balloons can be broken before reach the estimate.
        check = np.sort(t) - checker >= 0
        if np.all(check):
            r = estimate
        else:
            l = estimate + 1

    return r


if __name__ == '__main__':
    print(main())
