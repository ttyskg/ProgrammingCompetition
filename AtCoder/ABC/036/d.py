import sys

def dfs(tree, f, g, visited, root):
    chld = []
    for node in tree[root]:
        if visited[node]:
            continue

        chld.append(node)
        visited[node] = True

    if len(chld) == 0:
        g[root] = 1
        f[root] = 2

        return 1, 2

    f_ = 1
    g_ = 1
    for c in chld:
        if g[c] == 0:
            g[c], f[c] = dfs(tree, f, g, visited, c)

        g_ *= f[c]
        f_ *= g[c]

    g[root] = g_
    f[root] = g[root] + f_
    return g[root] % (10**9 + 7), f[root] % (10**9 + 7)


def main():
    input = sys.stdin.readline
    N = int(input())
    MOD = 10**9 + 7
    tree = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a, b = a-1, b-1

        tree[a].append(b)
        tree[b].append(a)

    f = [0] * N
    g = [0] * N
    start = 0
    visited = [False] * N
    visited[start] = True

    _, ans = dfs(tree, f, g, visited, start)

    return ans


if __name__ == '__main__':
    print(main())
