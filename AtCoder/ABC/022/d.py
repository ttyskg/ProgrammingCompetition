import numpy as np
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    A = np.array([tuple(map(int, input().split())) for _ in range(N)], dtype=np.float)
    B = np.array([tuple(map(int, input().split())) for _ in range(N)], dtype=np.float)

    A_weighted_center = np.sum(A, axis=0) / N
    B_weighted_center = np.sum(B, axis=0) / N

    A_dist_from_wc = np.sqrt(np.sum(np.square(A - A_weighted_center), axis=1))
    B_dist_from_wc = np.sqrt(np.sum(np.square(B - B_weighted_center), axis=1))

    A_farthest_point = np.max(A_dist_from_wc)
    B_farthest_point = np.max(B_dist_from_wc)

    return B_farthest_point / A_farthest_point


if __name__ == '__main__':
    print(main())
