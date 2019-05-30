# ref: https://atcoder.jp/contests/abc128/submissions/5654623

import sys
from bisect import bisect_left

def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    closure = []
    for _ in range(N):
        start, end, pos = map(int, input().split())
        closure.append((pos, start, end))

    closure.sort()

    D = [int(input()) for _ in range(Q)]

    ans = [-1] * Q
    skip = [-1] * Q
    for pos, start, end in closure:
        left = bisect_left(D, start - pos)
        right = bisect_left(D, end - pos)

        while left < right:
            if skip[left] == -1:
                ans[left] = pos
                skip[left] = right
                left += 1
            else:
                left = skip[left]

    return ans


if __name__ == '__main__':
    print(*main(), sep='\n')
