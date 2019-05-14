import sys
from itertools import combinations


def dfs(state, d=dict()):
    print(state)
    if max(state) == 1 and sum(state) == 1:  # Last one supplement.
        return 1

    if state in d:
        return d[state]

    remaining = []
    for i, s in enumerate(state):
        if s > 0:
            remaining.append(i)
    #remaining = [i for (i, s) in enumerate(state) is s > 0]
    cnt = 0
    n = 1
    while n <= len(remaining):
        for consumption in combinations(remaining, n):
            next_state = list(state)
            for i in consumption:
                next_state[i] -= 1

            cnt += dfs(tuple(next_state), d)

        n += 1

    cnt %= 10**9 + 7
    d[state] = cnt
    return cnt


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    supplements = [0] * M
    for _ in range(N):
        s = int(input())
        supplements[s-1] += 1

    state = tuple(supplements)
    return dfs(state)


if __name__ == '__main__':
    print(main())
