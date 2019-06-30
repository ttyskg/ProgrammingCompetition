import sys
import numpy as np
from scipy.sparse.csgraph import floyd_warshall

def main():
    input = sys.stdin.readline
    INF = 10**7
    N, M = map(int, input().split())
    d = np.full((N, N), INF)
    for i in range(N):
        d[i, i] = 0

    for _ in range(M):
        a, b, t = map(int, input().split())
        a, b, = a-1, b-1

        d[a, b] = t
        d[b, a] = t

    d = floyd_warshall(d)
    
    ans = INF
    for i in range(N):
        ans = min(ans, np.max(d[i, :]))

    return int(ans)


if __name__ == '__main__':
    print(main())
