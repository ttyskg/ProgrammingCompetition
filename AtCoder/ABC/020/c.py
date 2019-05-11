import numpy as np
import sys
from scipy.sparse.csgraph import floyd_warshall


def main():
    input = sys.stdin.readline
    H, W, T = map(int, input().split())
    N = H * W  # The number of nodes
    white = np.full((N, N), np.inf)
    for i in range(N):
        white[i, i] = 0
    black = np.full((N, N), np.inf)

    for i in range(H):
        for j, a in enumerate(map(str, input().strip())):
            n = i * W + j  # Node id: Up-left is 0, bottom-right is N-1.
            if a == '#':
                # Add edges start from black block.
                if j > 0:
                    black[n, n-1] = 1
                if j < W-1:
                    black[n, n+1] = 1
                if i > 0:
                    black[n, n-W] = 1
                if i < H - 1:
                    black[n, n+W] = 1

            else:
                if a == 'S':
                    start = n
                if a == 'G':
                    goal = n

                # Add edges start from white block.
                if j > 0:
                    white[n, n-1] = 1
                if j < W-1:
                    white[n, n+1] = 1
                if i > 0:
                    white[n, n-W] = 1
                if i < H - 1:
                    white[n, n+W] = 1

    left, right = 1, T
    mid = (left + right) // 2
    while right - left > 1:
        mid = (left + right) // 2

        # Calculate the shortest paths when the black edges' cost is mid.
        G = np.minimum(white, black * mid)
        G = floyd_warshall(G)

        if G[start, goal] > T:
            right = mid
        else:
            left = mid

    return left


if __name__ == '__main__':
    print(main())
