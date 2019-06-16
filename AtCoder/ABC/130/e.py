import sys

def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    n = min(N, M)
    ans = 1
    for i in range(1, n+1):
        ds = defaultdict(lambda: 0)
        dt = defaultdict(lambda: 0)

        for left in range(N - i + 1):
            key = tuple(S[left:left+i])
            ds[key] += 1

        for left in range(M - i + 1):
            key = tuple(T[left:left+i])
            dt[key] += 1

        for key in ds.keys():
            ans += ds[key] * dt[key]
            ans %= MOD

    return ans


if __name__ == '__main__':
    print(main())
