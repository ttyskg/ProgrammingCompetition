import sys

def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    N, B = map(int, input().split())
    R = N - B

    # Preparation for factorial table
    factrial = [1] * (N+1)
    for k in range(1, N+1):
        factrial[k] = (factrial[k-1] * k) % MOD

    # Preparation for inverse of factorial table
    fact_inv = [1] * (N+1)
    fact_inv[N] = pow(factrial[N], MOD - 2, MOD)
    for k in range(N-1, -1, -1):
        fact_inv[k] = (fact_inv[k+1] * (k+1)) % MOD

    def comb_mod(n, r, MOD=10**9+7):
        if n == 0 and r > 0:
            return 1
        if n < 0 or r < 0 or n < r:
            return 0
        return (factrial[n] * fact_inv[r] * fact_inv[n-r]) % MOD

    for q in range(1, B+1):
        ans = 0
        blue = comb_mod(B-1, B-q)

        # pattern 1: BR..B
        red1 = comb_mod(R-1, R-(q-1))
        ans += (blue * red1) % MOD
        ans %= MOD

        # pattern 2: BR...R or RB...B
        # The number of R and B is same
        red2 = comb_mod(R-1, R-q)
        ans += (2 * blue * red2) % MOD
        ans %= MOD

        # pattern 3: RB...R
        red3 = comb_mod(R-1, R-(q+1))
        ans += (blue * red3) % MOD
        ans %= MOD

        # Corner case
        if R == 0 and q == 1:
            ans = 1

        print(ans)


if __name__ == '__main__':
    main()
