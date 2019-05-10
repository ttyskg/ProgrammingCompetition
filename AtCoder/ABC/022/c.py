import numpy as np
import sys
from itertools import combinations
from scipy.sparse.csgraph import floyd_warshall


def main():
    input = sys.stdin.readline
    inf = 10**8
    N, M = map(int, input().split())
    d = np.full((N, N), inf, dtype=np.int)
    neighbors = []
    neighbors_cost = dict()
    for _ in range(M):
        u, v, cost = map(int, input().split())
        u, v = min(u, v), max(u, v)
        if u == 1:
            neighbors.append(v-1)
            neighbors_cost[v-1] = cost

        else:
            d[u-1, v-1] = cost
            d[v-1, u-1] = cost

    if len(neighbors) <= 1:
        return -1

    G = floyd_warshall(d)
    ans = inf
    for n1, n2 in combinations(neighbors, 2):
        ans = min(ans, G[n1, n2] + neighbors_cost[n1] + neighbors_cost[n2])

    if ans < inf:
        return int(ans)
    else:
        return -1


if __name__ == '__main__':
    print(main())
