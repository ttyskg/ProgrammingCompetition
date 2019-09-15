import sys
from heapq import heappush, heappop

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    heap = []
    for a in A:
        heappush(heap, -a)

    for _ in range(K):
        price = heappop(heap)
        heappush(heap,-(- price//2))

    return -sum(heap)


if __name__ == '__main__':
    print(main())
