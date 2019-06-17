import numpy as np
import sys

def rec_pow(k, n, mod):
    cnt = 1
    k1 = k
    while cnt * 2 <= n:
        k = np.mod(np.dot(k, k), mod)
        cnt *= 2

    if cnt == n:
        return k
    else:
        return np.mod(np.dot(k, rec_pow(k1, n-cnt, mod)), mod)


def main():
    input = sys.stdin.readline
    L, A, B, M = map(int, input().split())

    digits = [0] * 18
    cnt = 0
    for d in range(18):
        div = max(0, (10**(d+1) - 1 - A) // B)
        if 10**d <= A <= 10**(d+1):
            div += 1
        if div + cnt >= L:
            div = L - cnt
        if div == 0:
            continue

        digits[d] = div - cnt
        cnt += div
        print('cnt:', cnt, 'div:', div)
        if cnt >= L:
            break

    print(digits)
    k = np.identity(3, dtype=np.int64)
    for d in range(18):
        if digits[d] == 0:
            continue

        kd = np.array([[10**(d+1), 0, 0],\
                       [1, 1, 0],\
                       [0, B, 1]],\
                       dtype=np.int64)
        kd = np.mod(kd, M)
        k = np.dot(k, rec_pow(kd, digits[d], M))
        k = np.mod(k, M)
        print(k, '\n')

    s = np.array([0, A, 1])
    seq = np.mod(np.dot(s, k), M)
    return seq[0]

if __name__ == '__main__':
    print(main())
