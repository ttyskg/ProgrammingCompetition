import sys
from heapq import heappush, heappop

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    heap = []
    for i, b in enumerate(B):
        heappush(heap, (-b, i))

    cnt = 0
    if A == B:
        return 0
    while True:
        _, i = heappop(heap)
        i_l = (i - 1) % N
        i_r = (i + 1) % N

        n = B[i]
        m = B[i_l] + B[i_r]
        if n <= m:
            break

        cnt += n // m
        B[i] = n % m
        if A == B:
            return cnt
        heappush(heap, (-B[i], i))


    return -1


if __name__ == '__main__':
    print(main())
