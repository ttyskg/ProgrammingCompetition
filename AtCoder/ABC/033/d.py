from bisect import bisect_right, bisect_left
from math import pi, atan2
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    pos = [tuple(map(int, input().split())) for _ in range(N)]
    
    ERR = 1e-9
    right = 0
    obtuse = 0
    for ori in pos:
        angles = [atan2(a[1] - ori[1], a[0] - ori[0]) for a in pos if a != ori]
        angles = sorted(angles)
        angles += [a + 2*pi for a in angles]

        for i in range(N-1):
            base = angles[i]

            # s: start position of right angle
            s = bisect_left(angles, base + pi/2 - ERR)

            # t: end position of right angle
            t = bisect_right(angles, base + pi/2 + ERR)

            # u: end position of obtuse angle (180 degree)
            u = bisect_right(angles, base + pi)

            right += t - s
            obtuse += u - t

    total = N * (N-1) * (N-2) // 6
    acute = total - (right + obtuse)
    print(acute, right, obtuse)


if __name__ == '__main__':
    main()
