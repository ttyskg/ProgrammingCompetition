import numpy as np
import sys


def main():
    input = sys.stdin.readline
    R, C, K = map(int, input().split())
    A = [input().strip() for _ in range(R)]

    # Count the number of white tiles continuing from the top.
    T = [[0] * C for _ in range(R+1)]
    for i in range(1, R+1):
        for j in range(C):
            if A[i-1][j] == 'o':
                T[i][j] = T[i-1][j] + 1

    T = np.array(T)

    # Count the number of white tiles continuing from the bottom.
    B = [[0] * C for _ in range(R+1)]
    for i in range(R-1, -1, -1):
        for j in range(C):
            if A[i][j] == 'o':
                B[i][j] = B[i+1][j] + 1

    B = np.array(B)

    # The number of white tiles continuing in both the top and bottom
    # directions is the minimum value of the T and U.
    W = np.minimum(T[1:, :], B[:R, :])
    check = np.array(list(range(1, K)) + list(range(K, 0, -1)))
    cnt = 0
    for i in range(K-1, R-K+1):
        for j in range(K-1, C-K+1):
            if all(W[i, j-K+1:j+K] >= check):
                cnt += 1

    return cnt


if __name__ == '__main__':
    print(main())
