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
    MOD = 10**9 + 7
    X, Y = map(int, input().split())

    x1, x2 = 0, 0
    while min(X, Y) > 0:
        if 2*X == Y:
            x1 += X
            n = x1 + x2
            r = min(x1, x2)
            return comb_mod(n, r, MOD)
        
        elif X == 2*Y:
            x2 += Y
            n = x1 + x2
            r = min(x1, x2)
            return comb_mod(n, r, MOD)

        elif X >= Y:
            x2 += 1
            X -= 2
            Y -= 1
        
        else:
            x1 += 1
            X -= 1
            Y -= 2

    return 0

if __name__ == '__main__':
    print(main())