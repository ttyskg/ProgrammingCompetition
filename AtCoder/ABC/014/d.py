import sys
from collections import defaultdict, deque
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
    def make_tree(parent, node):
        for child in edges[node]:
            if child == parent:
                continue
            parents[child] = node
            depths[child] = depths[node] + 1
            make_tree(node, child)
    make_tree(0, 0)

    N2 = len(bin(N)) - 2
    doubling = [[0] * N2 for _ in range(N)]
    def make_doubling(node, parent):
        doubling[node][0] = parent
        for i in range(1, N2):
            doubling[node][i] = doubling[doubling[node][i-1]][i-1]
            if doubling[node][i] == 0:
                break
        for n in edges[node]:
            if n == parent:
                continue
            make_doubling(n, node)
    make_doubling(0, 0)

    print(doubling)
    return 0

    doubling = dict()
    for child in d[0]:
        doubling[child] = [0]

    visited = [False] * N
    visited[0] = True
    for child in d[0]:
        visited[child] = True
    q = deque()
    q.extend(d[0])









    for i in range(N):
        aa

    Q = int(input())
    for _ in range(Q):
        a, b = map(int, input().split())
        q = deque()
        q.append(a)
        print(bfs(d, q, b, 0, set()) + 1)


if __name__ == '__main__':
    main()
