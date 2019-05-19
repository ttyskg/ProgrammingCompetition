import sys
from itertools import accumulate

def main():
    input = sys.stdin.readline
    N = int(input())
    buy = [0] * (10**6 + 2)

    for _ in range(N):
        a, b = map(int, input().split())
        buy[a] += 1
        buy[b+1] -= 1

    buy = list(accumulate(buy))

    return max(buy)


if __name__ == '__main__':
    print(main())
