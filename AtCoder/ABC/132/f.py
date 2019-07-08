import sys

def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    N, K = map(int, input().split())
    n = int(N**(0.5))

    dp = [[0] * (n+1) for _ in range(K)]
    A = [0] * (n+1)
    for i in range(1, n+1):
        aa

    return n


if __name__ == '__main__':
    print(main())
