import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))

    ans = -2000
    for i in range(N):
        a = -2000
        t = -2000
        for j in range(N):
            if j == i:
                continue

            l, r = min(i, j), max(i, j)
            A_ = A[l:r+1]

            aoki = 0
            taka = 0
            for k, p in enumerate(A_, start=1):
                if k % 2 == 1:
                    taka += p
                else:
                    aoki += p

            if aoki > a:
                a = aoki
                t = taka

        ans = max(ans, t)

    return ans


if __name__ == '__main__':
    print(main())
