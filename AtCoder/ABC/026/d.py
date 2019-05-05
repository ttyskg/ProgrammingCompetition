import sys
from math import sin, pi

def f(A, B, C, t):
    return A*t + B*sin(C*t*pi)


def main():
    input = sys.stdin.readline
    A, B, C = map(int, input().split())

    err = 1e-6
    l, r = 0, 101
    mid = (l + r) / 2
    while not(100 - err < f(A, B, C, mid) < 100 + err):
        a = f(A, B, C, mid)
        if a >= 100 + err:
            r = mid
        
        if a <= 100 - err:
            l = mid

        mid = (l + r) / 2

    return mid


if __name__ == '__main__':
    print(main())
