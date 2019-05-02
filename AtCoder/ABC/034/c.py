import sys

def comb(n, r, factrial, fact_inv, MOD):
    if n < 0 or r < 0 or n < r:
        return 0
    else:
        return (factrial[n] * fact_inv[r] * fact_inv[n-r]) % MOD

def main():
    input = sys.stdin.readline
    W, H = map(int, input().split())
    MOD = 10**9 + 7
    N = W + H - 2
    r = min(W, H) - 1

    factrial = [1] * (N+1)
    for k in range(1, N+1):
        factrial[k] = (factrial[k-1] * k) % MOD

    fact_inv = [1] * (N+1)
    fact_inv[N] = pow(factrial[N], MOD - 2, MOD)
    for k in range(N-1, -1, -1):
        fact_inv[k] = (fact_inv[k+1] * (k+1)) % MOD

    return comb(N, r, factrial, fact_inv, MOD)


if __name__ == '__main__':
    print(main())
