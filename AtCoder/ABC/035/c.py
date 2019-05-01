import sys
from itertools import accumulate

def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = [0] * (N+1)
    for _ in range(Q):
        l, r = map(int, input().split())
        A[l-1] += 1
        A[r] -= 1

    ans = ''
    for i in accumulate(A):
        ans += str(i%2)

    return ans[:N]


if __name__ == '__main__':
    print(main())
