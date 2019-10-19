import sys
import numpy as np
from scipy.sparse.csgraph import floyd_warshall

def main():
    input = sys.stdin.readline
    N, M, L = map(int, input().split())
    d = [[float('inf')] * N for _ in range(N)]
    for i in range(N):
        d[i][i] = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        if c > L:
            continue
        d[a-1][b-1] = c
        d[b-1][a-1] = c
    
    G = floyd_warshall(d)

    e = [[float('inf')]*N for _ in range(N)]
    for i in range(N):
        e[i][i] = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if G[i][j] <= L:
                e[i][j] = 1
                e[j][i] = 1
    
    H = floyd_warshall(e)
    
    Q = int(input())
    for _ in range(Q):
        s, t = map(int, input().split())
        if H[s-1][t-1] == float('inf'):
            print(-1)
            continue
        ans = H[s-1][t-1] - 1
        print(int(ans))
    
    exit()


if __name__ == '__main__':
    print(main())