import sys

def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    L = str(input().strip())
    N = len(L)

    ans = pow(3, N, MOD)
    k = 1
    for i, b in enumerate(L, start=1):
        if b == '0':
            sub = k * 2 * pow(3, N-i, MOD) % MOD
            ans = (ans - sub) % MOD
        if b == '1':
            k = k * 2 % MOD
    return ans


if __name__ == '__main__':
    print(main())
