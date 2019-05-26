import sys
from heapq import heappush, heappop

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    heap = []
    ans = 0
    for a in map(int, input().split()):
        heappush(heap, a)

    BC = []
    for _ in range(M):
        B, C = map(int, input().split())
        BC.append((B, C))

    BC = sorted(BC, key=lambda x: -x[1])
    for B, C in BC:
        for _ in range(B):
            a = heappop(heap)
            if a < C:
                heappush(heap, C)
            else:
                heappush(heap, a)
                break

    return sum(heap)


if __name__ == '__main__':
    print(main())

