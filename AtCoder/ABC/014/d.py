import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    N = int(input())
    edges  = defaultdict(list)
    for _ in range(N-1):
        x, y = map(int, input().split())
        edges[x-1].append(y-1)
        edges[y-1].append(x-1)

    # Make a list of the tree structures.
    # parents[i] is parent of i-th node. The 0-th node is root.
    # depth[i] is depth of i-th node from 0-th node.
    parents = [0] * N
    depths = [0] * N
    visited = [False] * N
    def make_tree(node):
        visited[node] = True
        for child in edges[node]:
            if visited[child]:
                continue
            parents[child] = node
            depths[child] = depths[node] + 1
            make_tree(child)
    make_tree(0)

    B = 0
    while 2**B < N:
        B += 1
    doubling = [[0] * B for _ in range(N)]
    def make_doubling(node, parent):
        # Update doubling parents of targeted "node".
        doubling[node][0] = parent
        for i in range(1, B):
            doubling[node][i] = doubling[doubling[node][i-1]][i-1]
            if doubling[node][i] == 0:
                break
        # Recursive update for chiled node.
        for n in edges[node]:
            if n == parent:
                continue
            make_doubling(n, node)
    make_doubling(0, 0)

    def make_same_depth(a, b):
        # Node A is always more far from root than node B.
        if depths[a] < depths[b]:
            a, b = b, a

        i = 0
        diff = depths[a] - depths[b]
        while diff > 0:
            bit = 1 << i
            if diff & bit:
                a = doubling[a][i]
                diff ^= bit
            i += 1

        return a, b

    def find_lca(a, b):
        """ Find the lowest common ancestor of A and B."""
        a, b = make_same_depth(a, b)
        if a == b:
            return a

        def f(a, b):
            pa = parents[a]
            pb = parents[b]
            if pa == pb:
                return pa

            i = 1
            while doubling[a][i] != doubling[b][i]:
                i += 1

            a = doubling[a][i-1]
            b = doubling[b][i-1]
            return f(a, b)

        return f(a, b)

    Q = int(input())
    for _ in range(Q):
        ans = 0
        a, b = map(int, input().split())
        a, b = a-1, b-1

        lca = find_lca(a, b)
        print(depths[a] + depths[b] - 2 * depths[lca] + 1)


if __name__ == '__main__':
    main()
