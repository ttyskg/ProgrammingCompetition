import sys
from heapq import heappush, heappop, heapify


def dijkstra(s, links):
    """Dijkstra algorism
    s: int, start node.
    t: int, target node.
    links: iterable, link infomation.
           links[i] contains edges from node i: (cost, target_node).

    return int, minimal cost from s node to t node.
    """
    INF = 10**9
    dist = [INF] * len(links)
    dist[s] = 0

    heap = list(links[s])
    heapify(heap)
    while len(heap) > 0:
        cost, node = heappop(heap)
        if dist[node] < cost:
            continue

        dist[node] = cost

        for cost2, node2 in links[node]:
            if dist[node2] < cost + cost2:
                continue

            dist[node2] = cost + cost2
            heappush(heap, (cost + cost2, node2))

    return dist


def main():
    input = sys.stdin.readline
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    Gf = [set() for _ in range(N)]
    Gr = [set() for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        a, b = a-1, b-1
        Gf[a].add((c, b))
        Gr[b].add((c, a))

    minf = dijkstra(0, Gf)
    minr = dijkstra(0, Gr)
    ans = 0
    for i in range(N):
        res = (T - minf[i] - minr[i]) * A[i]
        ans = max(ans, res)

    return ans


if __name__ == '__main__':
    print(main())
