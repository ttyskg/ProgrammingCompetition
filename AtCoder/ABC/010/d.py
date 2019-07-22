import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    N, G, E = map(int, input().split())
    P = list(map(int, input().split()))

    edges = [[] for _ in range(N+1)]
    for _ in range(E):
        a, b = lap(int, input().split())
        edges[a].append(b)
        edges[b].append(a)

    for p in P:
        edges[N].append(p)
        edges[p].append(N)

    if G == 0:
        return 0
    if len(edges[0]) == 0:
        return 0
    



    return ans


if __name__ == '__main__':
    print(main())
