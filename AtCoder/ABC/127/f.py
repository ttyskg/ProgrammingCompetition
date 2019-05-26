import sys

def f(A, B):
    n = len(A)
    if n == 0:
        return (0, B)
    if n == 1:
        return (A[0] , B)

    A.sort()
    diff = 0
    for i in range(n-1):
        diff += A[i+1] - A[i]
    x = A[-2]
    return (x, diff + B)


def main():
    input = sys.stdin.readline
    INF = 10**9 + 1
    Q = int(input())
    A = []
    B = 0
    max_a =  -INF
    min_a = INF
    x = -INF
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            a, b = q[1], q[2]
            B += b
            if a > max_a:
                x = max_a
                max_a = a

            min_a = min(min_a, a)

        else:
            print('{} {}'.format(max(x, min_a), B + max_a - min_a))


if __name__ == '__main__':
    main()
