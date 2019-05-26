import sys
from itertools import accumulate

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    acc = [0] * (N+1)
    for _ in range(M):
        left, right = map(int, input().split())
        acc[left-1] += 1
        acc[right] -= 1

    cnt = 0
    for a in accumulate(acc):
        if a == M:
            cnt += 1

    return cnt


if __name__ == '__main__':
    print(main())
