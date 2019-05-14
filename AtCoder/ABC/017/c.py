import numpy as np
import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())

    total = 0
    jewels = np.zeros(M, dtype=np.int)
    for _ in range(N):
        left, right, score = map(int, input().split())
        jewels[left-1:right] += score
        total += score

    return total - jewels.min()


if __name__ == '__main__':
    print(main())
