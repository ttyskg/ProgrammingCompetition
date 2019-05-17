import sys
from itertools import accumulate

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())

    total = 0
    jewels = [0] * (M+1)
    for _ in range(N):
        left, right, score = map(int, input().split())
        jewels[left-1] += score
        jewels[right] -= score
        total += score

    return total - min(list(accumulate(jewels[:M])))


if __name__ == '__main__':
    print(main())
