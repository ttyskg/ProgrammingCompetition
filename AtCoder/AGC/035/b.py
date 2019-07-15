import sys
from collections import deque
from heapq import heappush, heappop

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    if M % 2 == 1:
        print(-1)
        return 0

    G = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    heap = []
    dist = [N] * (N+1)
    dist[1] = 0
    d = 0
    q = deque()
    q.append(1)
    while len(q) > 0:
        d += 1
        q_ = deque()
        while len(q) > 0:
            a = q.popleft()
            for b in G[a]:
                if dist[b] > d:
                    dist[b] = d
                    q_.append(b)
                    heappush(heap, (-d, b))
        q = q_

    cnt = [0] * (N+1)
    visited = [False] * (N+1)
    ans = []
    while len(heap) > 0:
        _, a = heappop(heap)
        visited[a] = True
        for b in G[a]:
            if visited[b]:
                continue

            if cnt[a] % 2 == 1:
                ans.append((a, b))
                cnt[a] += 1
            else:
                ans.append((b, a))
                cnt[b] += 1

    for a, b in ans:
        print('{} {}'.format(a, b))
    exit()


if __name__ == '__main__':
    main()
