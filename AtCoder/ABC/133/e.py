import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    N, K = map(int, input().split())
    G = defaultdict(list)
    for _ in range(N-1):
        a, b = map(int, input().split())
        a, b = a-1, b-1

        G[a].append(b)
        G[b].append(a)

    visited = [False] * N
    def dfs(n, ans):
        child = 1
        if n == 0:
            child = 0

        visited[n] = True
        for c in G[n]:
            if visited[c]:
                continue
            ans = (ans * (K - 1 - child)) % MOD
            ans = dfs(c, ans)
            child += 1

        return ans

    return dfs(0, K)


if __name__ == '__main__':
    print(main())
