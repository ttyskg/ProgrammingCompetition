import numpy as np
import sys
from scipy.sparse.csgraph import floyd_warshall


def main():
    input = sys.stdin.readline
    INF = 10**2
    N, M = map(int, input().split())

    d = np.full((N, N), INF)
    for i in range(N):
        d[i, i] = 0

    for _ in range(M):
        a, b = map(int, input().split())
        d[a-1, b-1] = 1
        d[b-1, a-1] = 1

    G = floyd_warshall(d)
    ans = np.sum(G == 2, axis=0)
    return ans


if __name__ == '__main__':
    print(*main(), sep='\n')
