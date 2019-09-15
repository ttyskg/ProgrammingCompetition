import sys

def main():
    input = sys.stdin.readline
    N, K, Q = map(int, input().split())
    P = [0] * N
    for _ in range(Q):
        a = int(input())
        P[a-1] += 1

    for p in P:
        if p > Q - K:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
