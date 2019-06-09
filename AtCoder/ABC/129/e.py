import sys

def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    L = str(input().strip())
    N = len(L)

    dp0 = 0  # Less than L
    dp1 = 1  # Can be greater than L
    for b in L:
        if b == '0':
            # dp1 = dp1 * 1
            dp0 = dp0 * 3 % MOD
        if b == '1':
            dp0 = (dp0 * 3 + dp1) % MOD
            dp1 = dp1 * 2 % MOD
    return (dp0 + dp1) % MOD


if __name__ == '__main__':
    print(main())
