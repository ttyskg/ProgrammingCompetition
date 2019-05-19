import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)

def bfs(d, q, b, cnt=0, visited=set()):
    q_ = deque()
    while len(q) > 0:
        s = q.popleft()
        if s == b:
            return cnt

        visited.add(s)
        for t in d[s]:
            if t in visited:
                continue

            q_.append(t)

    return bfs(d, q_, b, cnt+1, visited)


def main():
    input = sys.stdin.readline
    N = int(input())
    d = defaultdict(list)
    for _ in range(N-1):
        x, y = map(int, input().split())
        d[x-1].append(y-1)
        d[y-1].append(x-1)

    # Make table of distance from 0-th node:
    # dist[i] means the distance between 0-th node and i-th node.
    dist = [0] * N
    q = deque()
    q.append(0)
    visited = set()
    cnt = 0
    while len(q) > 0:
        q_ = deque()
        while len(q) > 0:
            s = q.popleft()
            dist[s] = cnt

            visited.add(s)
            for t in d[s]:
                if t in visited:
                    continue

                q_.append(t)

        q = q_
        cnt += 1

    doubling









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
