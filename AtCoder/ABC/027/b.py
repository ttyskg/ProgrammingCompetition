import sys
from itertools import accumulate

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))

    acc = list(accumulate(A))
    total = acc[N-1]
    if total % N != 0:
        return -1

    u = total // N
    cnt = 0
    for i, a in enumerate(acc, start=1):
        if a == u * i:
            continue
        cnt += 1

    return cnt


if __name__ == '__main__':
    print(main())
