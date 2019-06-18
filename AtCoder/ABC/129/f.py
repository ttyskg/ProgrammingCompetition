import sys


def dot(A, B, mod):
    r = len(A)
    c = len(B[0])
    m = len(A[0])
    res = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            for k in range(m):
                res[i][j] += (A[i][k] * B[k][j]) % mod
                res[i][j] %= mod
    return res


def rec_pow(k, n, mod):
    if n == 1:
        return k

    k2 = dot(k, k, mod)
    if n % 2 == 0:
        return rec_pow(k2, n//2, mod)
    else:
        return dot(rec_pow(k2, n//2, mod), k, mod)


def main():
    input = sys.stdin.readline
    L, A, B, M = map(int, input().split())

    cnt = 0
    s = [[0, A%M, 1]]
    for d in range(1, 19):
        n = 0
        if 10**(d-1) <= A <= 10**d:
            n += 1

        div = max(0, (10**d - 1 - A) // B)
        div = min(div, L-1)
        n += div - cnt
        if n == 0:
            continue

        k = [[pow(10, d, M), 0, 0],\
             [1, 1, 0],\
             [0, B%M, 1]]
        s = dot(s, rec_pow(k, n, M), M)

        cnt = div
        if cnt >= L-1:
            break

    return s[0][0]

if __name__ == '__main__':
    print(main())
