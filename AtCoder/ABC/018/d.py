import numpy as np
import sys
from itertools import combinations

def main():
    input = sys.stdin.readline
    N, M, P, Q, R = map(int, input().split())
    chocolates = np.zeros((N, M), dtype=np.int)

    for _ in range(R):
        g, b, c = map(int, input().split())
        g, b = g-1, b-1  # 0-index for girls and boys ID.

        # choco[i, j] means happiness when girl i can give boy j chocolate.
        chocolates[g, b] += c

    ans = 0
    for girls in combinations(range(N), P):
        # The happiness of each boy when all girls in "girls" give out choco.
        happiness = chocolates[girls, :].sum(axis=0)
        # In this "girls" group, the maximum happiness is achieved when
        # boys within the top Q rank of happiness score form a group.
        score = np.sum(np.sort(happiness)[::-1][:Q])
        ans = max(ans, score)

    return ans


if __name__ == '__main__':
    print(main())
