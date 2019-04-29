import sys


def gcd(a, b):
    """Euclidean Algorithm"""
    a, b = max(a, b), min(a, b)
    while b != 0:
        a, b = b, a % b
    return a


def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))

    L = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        L[i] = gcd(L[i-1], A[i-1])

    R = [0 for _ in range(N+1)]
    for i in range(N-1, -1, -1):
        R[i] = gcd(R[i+1], A[i])

    M = [0 for _ in range(N)]
    for i in range(N):
        M[i] = gcd(L[i], R[i+1])

    return max(M)


if __name__ == '__main__':
    print(main())
