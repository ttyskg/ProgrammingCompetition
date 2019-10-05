import sys
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
sys.setrecursionlimit(10**7)


def main():
    input = sys.stdin.readline
    N = int(input())
    G = []
    for _ in range(N):
        S = [int(c) for c in str(input().strip())]
        T = []
        for i, e in enumerate(S):
            if e == 1:
                T.append(i)
        G.append(T)
    
    colors = [-1] * N
    visited = [False] * N
    def is_binarygraph(v, color):
        visited[v] = True
        for n in G[v]:
            if colors[n] == color:
                return False
            if visited[n]:
                continue
            colors[n] = (color + 1) % 2
            if not is_binarygraph(n, colors[n]):
                return False
        return True
    
    colors[0] = 0
    if not is_binarygraph(0, 0):
        return -1

    inf = 10**3
    d = [[inf]*N for _ in range(N)]
    for i in range(N):
        for j in G[i]:
            d[i][j] = 1
    for i in range(N):
        d[i][i] = 0
    
    fw = floyd_warshall(d)
    return np.max(fw) + 1

if __name__ == '__main__':
    print(int(main()))