import sys

def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    N, K = map(int, input().split())
    n = int(N**(0.5))

    dp = [[0] * n for _ in range(K)]

    return n


if __name__ == '__main__':
    print(main())
