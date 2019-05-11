import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    N = int(input())
    a, b = map(int, input().split())
    start, goal = a-1, b-1

    edges = defaultdict(list)
    M = int(input())
    for _ in range(M):
        s, t = map(int, input().split())
        edges[s-1].append(t-1)
        edges[t-1].append(s-1)

    # The number of times node i appears in the shortest paths from A to B.
    dp = [0] * N
    dp[start] = 1

    starts = deque()
    starts.append(start)
    visited = set()
    while True:
        dests = set()
        dp_ = [0] * N
        while len(starts) > 0:
            s = starts.popleft()
            if s in visited:
                continue
            visited.add(s)

            for dest in edges[s]:
                dp_[dest] += dp[s]
                dp_[dest] %= MOD

                dests.add(dest)

        if goal in dests:
            return dp_[goal]

        starts = deque()
        starts.extend(dests)
        dp = dp_


if __name__ == '__main__':
    print(main())
