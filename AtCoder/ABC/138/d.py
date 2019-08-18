import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    G = [set() for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].add(b-1)
        G[b-1].add(a-1)

    weights = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        weights[p-1] += x

    ans = [0] * N
    ans[0] = weights[0]
    visited = [False] * N
    def f(a, node):
        visited[node] = True
        for nt in G[node]:
            if visited[nt]:
                continue
            b = a + weights[nt]
            ans[nt] = b
            f(b, nt)
        return  0

    f(weights[0], 0)
    return ' '.join(map(str, ans))


if __name__ == '__main__':
    print(main())
