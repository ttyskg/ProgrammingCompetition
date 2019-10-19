import sys
from itertools import combinations
from bisect import bisect_left

def main():
    input = sys.stdin.readline
    N = int(input())
    L = list(map(int, input().split()))

    L = sorted(L)
    ans = 0
    for a, b in combinations(range(N), 2):
        a, b = min(a, b), max(a, b)

        c_max = L[a] + L[b]

        left = b + 1
        right = bisect_left(L, c_max)

        ans += right - left

    return ans

if __name__ == '__main__':
    print(main())