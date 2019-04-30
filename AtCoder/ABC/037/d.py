import sys
sys.setrecursionlimit(3000)


def f(A, i, j, memo):
    if memo[i][j] != 0:
        return memo[i][j]

    res = 1
    H, W = len(A), len(A[0])
    for s, t in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if 0 <= i+s < H and 0 <= j+t < W and A[i][j] < A[i+s][j+t]:
            res += f(A, i+s, j+t, memo)

    res %= 10**9 + 7
    memo[i][j] = res
    return res 


def main():
    input = sys.stdin.readline
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    memo = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if memo[i][j] == 0:
                f(A, i, j, memo)

    MOD = 10**9 + 7
    ans = sum(sum(m) % MOD for m in memo)
    return ans % MOD


if __name__ == '__main__':
    print(main())
