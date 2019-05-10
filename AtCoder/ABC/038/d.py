#ref: https://atcoder.jp/contests/abc038/submissions/747025

import sys
from bisect import bisect_left


def main():
    input = sys.stdin.readline
    N = int(input())

    box = [tuple(map(int, input().split())) for _ in range(N)]
    box = sorted(box, key=lambda x: (x[0], -x[1]))
    W = [w for _, w in box]

    inf = max(W) + 1
    nested = [inf] * N

    # The largest index of the non-INF int is equal to the number of nesting.
    for w in W:
        i = bisect_left(nested, w)
        nested[i] = w

    max_nest = bisect_left(nested, inf)
    return max_nest


if __name__ == '__main__':
    print(main())
