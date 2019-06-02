import sys

def main():
    input = sys.stdin.readline
    MOD = 10**6 + 3

    factrial = [1] * (MOD)
    for k in range(1, MOD):
        factrial[k] = (factrial[k-1] * k) % MOD
    
    fact_inv = [1] * (MOD)
    fact_inv[MOD-1] = pow(factrial[MOD-1], MOD - 2, MOD)
    for k in range(MOD-2, -1, -1):
        fact_inv[k] = (fact_inv[k+1] * (k+1)) % MOD

    Q = int(input())
    for _ in range(Q):
        x, d, n = map(int, input().split())

        if d == 0:
            ans = pow(x, n, MOD)

        else:
            y = x * pow(d, MOD-2, MOD) % MOD

            if y + n - 1 >= MOD:
                ans = 0

            else:
                ans = (factrial[y+n-1] * fact_inv[y-1] * pow(d, n, MOD)) % MOD

        print(ans)


if __name__ == '__main__':
    main()
