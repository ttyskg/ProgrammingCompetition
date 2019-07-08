import sys


def main():
    input = sys.stdin.readline
    B = 30  # 2**30 > 10**9
    N, M, D = map(int, input().split())
    A = list(map(int, input().split()))

    start = [i for i in range(N)]
    goal = [i for i in range(N)]
    for i in A:
        goal[i-1], goal[i] = goal[i], goal[i-1]

    doubling = [[0] * B for _ in range(N)]
    for i, g in enumerate(goal):
        doubling[g][0] = i

    for i in range(1, B):
        for j in range(N):
            n = doubling[j][i-1]
            doubling[j][i] = doubling[n][i-1]

    b = 0
    ans = [i for i in range(N)]
    while D > 0:
        bit = 1 << b
        if D & bit == 0:
            b += 1
            continue

        tmp = [0] * N
        for i, n in enumerate(ans):
            tmp[i] = doubling[n][b]
        ans = tmp

        b += 1
        D ^= bit

    for n in ans:
        print(n+1)


if __name__ == '__main__':
    main()
