import sys
from collections import defaultdict, deque


def main():
    input = sys.stdin.readline
    d = defaultdict(list)
    N = int(input())
    ans = [0] * N
    for _ in range(N-1):
        a, b = map(int, input().split())
        d[a-1].append(b-1)
        d[b-1].append(a-1)

    C = list(map(int, input().split()))
    C = sorted(C, key=lambda x: -x)
    score = sum(C[1:])

    ans[0] = C[0]
    cnt = 1
    visited = set([0])
    q = deque()
    q.extend(d[0])
    while len(q) > 0:
        a = q.popleft()

        if a in visited:
            continue

        ans[a] = C[cnt]
        visited.add(a)
        cnt += 1

        q.extend(d[a])

    print(score)
    print(*ans, sep=' ')


if __name__ == '__main__':
    main()
