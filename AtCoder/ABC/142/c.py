import sys
from heapq import heappush, heappop

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    heap = []
    for i, a in enumerate(A, start=1):
        heappush(heap, (a, i))
    
    ans = []
    while heap:
        _, a = heappop(heap)
        ans.append(a)

    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()