import sys
from itertools import accumulate

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    acc = list(accumulate(A))

    cnt = 0
    left, right = 0, 0
    while right < N:
        while acc[right] - acc[left] < K and right < N:
            right += 1

        while acc[right] - acc[left] >= K:
            cnt += N + 1 - right
            left += 1

    return cnt


if __name__ == '__main__':
    print(main())
