import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    N = int(input())
    d = defaultdict(list)
    for _ in range(N-1):
        x, y = map(int, input().split())
        d[x-1].append(y-1)
        d[y-1].append(x-1)

    # Make a list of the tree structures.
    # tree[i] = (depth, parent)
    tree  = [0] * N  # parent, depth
    q = deque()
    q.append((-1, 0))
    visited = [False] * N
    depth  = 0
    while len(q) > 0:
        q_ = deque()
        while len(q) > 0:
            parent, child =  q.popleft()
            tree[child] = (depth, parent)
            visited[child] = True
            for gc in d[child]:
                if visited[gc]:
                    continue
                q_.append((child, gc))
        q = q_
        depth  += 1

    def dfs(n):
        depth, parent = tree[n]
        if parent in doubling:
            doubling[n] =


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
