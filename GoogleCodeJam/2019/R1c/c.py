import numpy as np
import sys


def solve():
    R, C = map(int, input().split())
    A = [[0 if c == '.' else -1 for c in input().strip()] for _ in range(R)]
    A = np.array(A)


def main():
    input = sys.stdin.readline
    T = int(input())
    for t in range(1, T+1):
        ans = solve()
        print('Case #{}: {}'.format(t, ans))

if __name__ == '__main__':
    print(main())
