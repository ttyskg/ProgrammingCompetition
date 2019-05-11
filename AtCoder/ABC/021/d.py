import sys


def comb_mod(n, r, MOD=10**9+7):
    if n < 0 or r < 0 or n < r:
        return 0

    factrial = [1] * (n+1)
    for k in range(1, n+1):
        factrial[k] = (factrial[k-1] * k) % MOD

    fact_inv = [1] * (n+1)
    fact_inv[n] = pow(factrial[n], MOD - 2, MOD)
    for k in range(n-1, -1, -1):
        fact_inv[k] = (fact_inv[k+1] * (k+1)) % MOD

    return (factrial[n] * fact_inv[r] * fact_inv[n-r]) % MOD


def main():
    input = sys.stdin.readline
    N = int(input())
    K = int(input())

    #The answer is equal to nHk (combination with repetition).
    #    nHk = n+k-1Cn-1
    return comb_mod(N+K-1, N-1)


if __name__ == '__main__':
    print(main())
