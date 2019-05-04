import sys
from itertools import accumulate

def main():
    input = sys.stdin.readline
    H, W, N = map(int, input().split())
    r, c = map(int, input().split())
    S = str(input().strip())
    T = str(input().strip())

    R = c
    L = c
    U = r
    D = r

    i = 0
    while i < N:
        s, t = S[i], T[i]

        if s == 'R':
            R += 1
        elif s == 'L':
            L -= 1
        elif s == 'U':
            U -= 1
        else:
            D += 1

        if R > W or L <= 0 or U <= 0 or D > H:
            return 'NO'

        if t == 'R':
            L += 1
            L = min(L, W)
        elif t == 'L':
            R -= 1
            R = max(R, 1)
        elif t == 'U':
            D -= 1
            D = max(D, 1)
        else:
            U += 1
            U = min(U, H)

        i += 1

    return 'YES' 


if __name__ == '__main__':
    print(main())
