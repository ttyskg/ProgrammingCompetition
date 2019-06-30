import sys

def main():
    input = sys.stdin.readline
    N, D = map(int, input().split())
    X, Y = map(int, input().split())

    if abs(X) % D != 0 or abs(Y) % D != 0:
        return 0

    minx = abs(X) // D
    miny = abs(Y) // D

    if minx + miny > N:
        return 0

    if (N - (minx + miny)) % 2 == 1:
        return 0
    # The number of jumps for adjustment.
    M = (N - (minx + miny)) // 2

    pascal = [[0] * (N+1) for _ in range(N+1)]
    pascal[0][0] = 1
    pascal[1][0] = 1
    pascal[1][1] = 1
    for i in range(2, N+1):
        pascal[i][0] = 1
        for j in range(1, i+1):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    num = 0
    # X direction adjustment.
    for i in range(M + 1):
        x = minx + 2*i
        y = miny + 2*(M - i)

        x_num = pascal[x][i]
        y_num = pascal[y][M - i]
        direct_num = pascal[N][x]

        num += x_num * y_num * direct_num

    return num / 4**N


if __name__ == '__main__':
    print(main())
