import sys
from collections import deque
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
    S, T = map(int, input().split())
    S, T = S-1, T-1

    q = deque()
    q.append(S)
    cnt = 0
    cnt_k = 0
    visited = [False] * N
    visited[S] = True
    while len(q) > 0:
        cnt += 1
        if cnt % 3 == 0:
            cnt_k += 1

        next_ = set()
        while len(q) > 0:
            n0 = q.pop()
            for n1 in G[n0]:
                if cnt % 3 == 0:
                    if n1 == T:
                        return cnt_k

                    if visited[n1]:
                        continue

                    visited[n1] = True

                next_.add(n1)

        q = deque()
        q.extend(list(next_))

    return -1


if __name__ == '__main__':
    print(main())
