import numpy as np
import sys

def main():
    input = sys.stdin.readline
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        S = [0 if c == '#' else 1 for c in input().strip()]
        A.append(S)

    A = np.array(A)
    up = np.zeros((H+1, W), dtype=np.int)
    down = np.zeros((H+1, W), dtype=np.int)
    right = np.zeros((H, W+1), dtype=np.int)
    left = np.zeros((H, W+1), dtype=np.int)

    for i in range(1, H+1):
        up[i] = (up[i-1] + 1) * A[i-1]
        down[H-i] = (down[H-i+1] + 1) * A[H-i]

    for i in range(1, W+1):
        right[:, i] = (right[:, i-1] + 1) * A[:, i-1]
        left[:, W-i] = (left[:, W-i+1] + 1) * A[:, W-i]

    R = (up[1:] + down[:H] - 1) * A
    C = (right[:, 1:] + left[:, :W] - 1) * A
    W = (R + C - 1) * A
    return W.max()


if __name__ == '__main__':
    print(main())
