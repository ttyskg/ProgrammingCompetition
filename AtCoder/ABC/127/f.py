import sys
from heapq import heappop, heappush


def main():
    input = sys.stdin.readline
    INF = 10**9 + 1
    Q = int(input())
    left = []
    right = []
    min_val = 0
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            a, b = q[1], q[2]

            # Update median
            heappush(left, -a)
            heappush(right, a)

            left_max = -heappop(left)
            right_min = heappop(right)

            heappush(left, -min(left_max, right_min))
            heappush(right, max(left_max, right_min))

            # Update minimum value of f(x)
            min_val += abs(right_min - left_max)
            min_val += b

        else:
            median = -heappop(left)
            print('{} {}'.format(median, min_val))

            heappush(left, -median)


if __name__ == '__main__':
    main()
