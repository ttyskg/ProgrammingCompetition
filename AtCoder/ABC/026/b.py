import sys
from math import pi

def main():
    input = sys.stdin.readline
    N = int(input())
    R = [int(input()) for _ in range(N)]
    R = sorted(R, key=lambda x: -x)

    red = 0
    white = 0
    for i, r in enumerate(R, start=1):
        area = r**2 * pi
        if i % 2 == 1:
            red += area
        else:
            white += area

    return red - white


if __name__ == '__main__':
    print(main())
