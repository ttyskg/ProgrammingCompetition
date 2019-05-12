import sys
from itertools import combinations


def get_divisors(K):
    divs = set()
    for i in range(1, int(K**0.5)+1):
        if K % i == 0:
            divs.add(i)
            divs.add(K//i)

    return divs


def get_prime_factors(n):
    res = []
    p = 2
    while p**2 <= n:
        if n % p == 0:
            res.append(p)

            while n % p == 0:
                n //= p

        p += 1
    
    if n > 1:
        res.append(n)

    return res


def sum_series(limit, common_diff):
    n = limit // common_diff
    return n * (n+1) * common_diff // 2


def sum_lcm1(N, K):
    prime_factors = get_prime_factors(K)
    S = sum_series(N, 1)

    # Substract for numbers where the GCD with the K is not 1.
    # In according to the inclusion-exclusion principle, add numbers which are 
    # substrated multi-times.
    pf_num = len(prime_factors)
    for n in range(1, pf_num+1):
        sign = (-1)**n
        for factors in combinations(prime_factors, n):
            p = 1
            for f in factors:
                p *= f

            S += sign * sum_series(N, p)

    return S * K


def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    N, K = map(int, input().split())

    ans = 0
    divisors = get_divisors(K)
    for div in divisors:
        ans += sum_lcm1(N//div, K//div) * div
        ans %= MOD

    return ans


if __name__ == '__main__':
    print(main())
