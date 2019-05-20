import sys

def main():
    input = sys.stdin.readline
    M, K = map(int, input().split())

    if K >= 2**M:
        return [-1]

    if M == 1:
        if K == 0:
            return [0, 0, 1, 1]
        else:
            return [-1]

    # [0, 1, ..., 2**M - 1] excepting K
    a = list(range(K)) + list(range(K+1, 2**M))

    # [2**M - 1, 2**M - 2, ..., 1, 0] excepting K
    b = a[::-1]

    return a + [K] + b + [K]


if __name__ == '__main__':
    print(*main())
