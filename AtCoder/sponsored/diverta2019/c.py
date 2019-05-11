import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    ans = 0
    ba = 0  # Num. of str that the first letter is B and the last one is A.
    xa = 0  # Num. of str that the last letter is A and the first one is not B.
    bx = 0  # Num. of str that the first letter is B and the last one is not A.
    for _ in range(N):
        s = str(input().strip())

        # Count the number of AB contained in the initial strings.
        for i in range(len(s)):
            if s[i:i+2] == 'AB':
                ans += 1

        if s[0] == 'B' and s[-1] == 'A':
            ba += 1
        elif s[-1] == 'A':
            xa += 1
        elif s[0] == 'B':
            bx += 1

    if ba == 0:
        # One xa ans one bx make one new "AB".
        #   xa + bx -> xABx
        ans += min(xa, bx)

    elif max(xa, bx) == 0:
        # N of ba make N-1 new "AB".
        # BxxA + BxxA + ... + BxxA -> BxxABxxAB...ABxxA
        ans += ba - 1

    else:  # There is at least one bx or ax and at least one ba.
        # N of ba make N-1 new "AB" and a ba.
        #   ba + ba + ... + ba -> baba...ba = ba
        # The last remaining ba and bx/ax make a new "AB" and a new bx/ax.
        #   ba + bx -> bABx = bx,  xa + ba -> xABa = xa
        # Then, bx and xa make a new "AB".
        #   xa + bx -> xABx 
        ans += ba + min(xa, bx)

    return ans


if __name__ == '__main__':
    print(main())
