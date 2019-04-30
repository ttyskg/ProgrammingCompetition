import sys
sys.setrecursionlimit(10000)


def f(A, i, j, memo):
    if memo[i][j] != -1:
        return memo

    if A[i][j] >= max(A[i-1][j], A[i+1][j], A[i][j-1], A[i][j+1]):
        memo[i][j] = 1
        return memo

    ans = 1
    for s, t in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if A[i][j] < A[i+s][j+t]:
            memo = f(A, i+s, j+t, memo)
            ans += memo[i+s][j+t]

    memo[i][j] = ans
    return memo


def main():
    input = sys.stdin.readline
    H, W = map(int, input().split())
    A = []
    A.append([0 for _ in range(W+2)])
    for _ in range(H):
        a = [0] + list(map(int, input().split())) + [0]
        A.append(a)
    A.append([0 for _ in range(W+2)])

    MOD = 10**9 + 7
    memo = [[-1 for _ in range(W+2)] for _ in range(H+2)]

    ans = 0
    for i in range(1, H+1):
        for j in range(1, W+1):
            if memo[i][j] != -1:
                ans += memo[i][j]
                ans %= MOD
            else:
                memo = f(A, i, j, memo)
                ans += memo[i][j]
                ans %= MOD

    return ans % MOD


if __name__ == '__main__':
    print(main())
