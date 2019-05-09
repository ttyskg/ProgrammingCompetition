import sys


def get_inverse(n, mod):
    i = mod - 2
    res = 1
    while i > 0:
        if i % 2 == 1:
            res *= n
            res %= mod

        n **= 2
        n %= mod
        i //= 2

    return res


def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    A = int(input())
    B = int(input())
    C = int(input())

    # r = (BC - CA) / (AB - BC + CA)
    # c = (BC - AB) / (AB - BC + CA)

    # According to Fermat's little theorem,
    # a^(-1) = a^(p-2) (mod p)

    r_numerator = (B*C - C*A) % MOD
    c_numerator = (B*C - A*B) % MOD
    denominator = A*B - B*C + C*A
    den_inverse = get_inverse(denominator, MOD)

    r = (r_numerator * den_inverse) % MOD
    c = (c_numerator * den_inverse) % MOD

    return r, c


if __name__ == '__main__':
    print(*main())
