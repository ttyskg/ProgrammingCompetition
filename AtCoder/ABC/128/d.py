import sys
from heapq import heappop, heappush

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    V = list(map(int, input().split()))

    ans = 0
    for left in range(min(N, K) + 1):
        for right in range(min(N, K) - left + 1):
            heap = []
            for v in V[:left]:
                heappush(heap, v)

            for v in V[N - right:]:
                heappush(heap, v)

            cnt = left + right
            while cnt < K and len(heap) > 0:
                v = heappop(heap)
                if v >= 0:
                    heappush(heap, v)
                    break

                cnt += 1

            ans = max(ans, sum(heap))

    return ans


if __name__ == '__main__':
    print(main())
