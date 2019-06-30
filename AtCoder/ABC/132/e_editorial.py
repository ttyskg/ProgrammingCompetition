import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    G = [[] for _ in range(3*N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u, v = u-1, v-1

        G[3*u].append(3*v+1)
        G[3*u+1].append(3*v+2)
        G[3*u+2].append(3*v)

    S, T = map(int, input().split())
    S, T = 3*(S-1), 3*(T-1)

    cnt = 0
    q = deque()
    q.append(S)
    visited = [False] * (3*N)
    visited[S] = True
    while len(q) > 0:
        q_ = deque()
        cnt += 1
        while len(q) > 0:
            n = q.pop()
            for m in G[n]:
                if visited[m]:
                    continue

                if m == T:
                    return cnt // 3

                visited[m] = True
                q_.append(m)

        q = q_

    return -1


if __name__ == '__main__':
    print(main())
