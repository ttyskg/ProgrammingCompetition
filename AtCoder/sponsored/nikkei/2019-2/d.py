import sys
from heapq import heappop, heappush, heapify

def dijkstra(s, t, links):
    """Dijkstra algorism
    s: int, start node.
    t: int, target node.
    links: iterable, link infomation.
           links[i] contains edges from node i: (cost, target_node).

    return int, minimal cost from s node to t node.
    """
    heap = list(links[s])
    heapify(heap)
    visited = set()
    while len(heap) > 0:
        cost, node = heappop(heap)
        if node == t:
            return cost

        if node in visited:
            continue

        visited.add(node)
        for cost2, node2 in links[node]:
            if node2 in visited:
                continue

            heappush(heap, (cost + cost2, node2))

    return -1

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    links = [[] for _ in range(N)]
    for i in range(1, N):
        links[i].append((0, i-1))

    for _ in range(M):
        l, r, c = map(int, input().split())
        links[l-1].append((c, r-1))
    
    return dijkstra(0, N-1, links)
    

if __name__ == '__main__':
    print(main())