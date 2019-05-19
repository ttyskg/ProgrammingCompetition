import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.readline
    N = int(input())
    d = defaultdict(list)
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        d[u-1].append((v-1, w))
        d[v-1].append((u-1, w))

    dist = [0] * N
    q = deque()
    q.append((0, 0))
    visited = set()

    while len(q) > 0:
        q_ = deque()
        while len(q) > 0:
            node1, cost1 = q.popleft()

            dist[node1] = cost1
            visited.add(node1)

            for node2, cost2 in d[node1]:
                if node2 in visited:
                    continue

                q_.append((node2, cost1 + cost2))

        q = q_

    for d in dist:
        print(d % 2)


if __name__ == '__main__':
    main()
