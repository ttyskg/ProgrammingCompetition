import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    N, H = map(int, input().split())
    A, B, C, D, E = map(int, input().split())

    if N * E < H:
        return 0

    # The number of eating when eating only normal meal.
    n = (N*E - H) // (B + E) + 1
    ans = n * A

    # m is the number of poor meals required when
    # eating normal meal i times.
    for i in range(n):
        health = H + i * B
        m = ((N - i) * E - health) // (D + E) + 1
        ans = min(ans, i * A + m * C)

    return ans


if __name__ == '__main__':
    print(main())
