import sys
from itertools import accumulate

def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = [0 for _ in range(N)]
    for _ in range(Q):
        l, r, t = map(int, input().split())
        A[l-1] += t
        A[r] -= t

    A = list(accumulate(A))
    return print(*A)


if __name__ == '__main__':
    main()
