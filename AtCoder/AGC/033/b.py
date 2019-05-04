import sys

def main():
    input = sys.stdin.readline
    H, W, N = map(int, input().split())
    ini_r, ini_c = map(int, input().split())
    S = str(input().strip())[::-1]
    T = str(input().strip())[::-1]

    dp = [0] * (N+1)
    dp[0] = (1, H, 1, W)
    for i in range(N):
        s, t, = S[i], T[i]
        d, u, l, r = dp[i]

        if t == 'L':
            r = min(W, r+1)
        elif t == 'R':
            l = max(1, l-1)
        elif t == 'U':
            u = min(H, u+1)
        else:
            d = max(1, d-1)

        if s == 'L':
            l += 1
        elif s == 'R':
            r -= 1
        elif s == 'U':
            d += 1
        else:
            u -= 1

        if u < d or r < l:
            return 'NO'

        dp[i+1] = (d, u, l, r)

    d, u, l, r = dp[N]
    if not(d <= ini_r <= u and l <= ini_c <= r):
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':
    print(main())
