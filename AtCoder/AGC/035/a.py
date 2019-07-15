import sys
from collections import Counter

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))

    c = Counter(A)
    # All caps are 0.
    if 0 in c and len(c) == 1:
        return 'Yes'

    # N/3 '0', and 2N/3 'non-zero'.
    if 0 in c and len(c) == 2:
        v0 = c[0]
        for k, v in c.items():
            if k != 0 and v == 2 * v0:
                return 'Yes'

    # Three caps.
    if len(c) == 3:
        x, y, z = tuple(c.keys())
        if (x ^ y) == z and c[x] == c[y] == c[z]:
            return 'Yes'

    return 'No'


if __name__ == '__main__':
    print(main())
