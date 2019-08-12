import sys
from collections import defaultdict
from heapq import heappop, heappush

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    d = defaultdict(list)
    for _ in range(N):
        a, b = map(int, input().split())
        d[a].append(-b)

    ans = 0
    heap = []
    for i in range(1, M+1):
        for b in d[i]:
            heappush(heap, b)
        if heap:
            ans -= heappop(heap)

    return ans


if __name__ == '__main__':
    print(main())
