import sys

def main():
    input = sys.stdin.readline
    N, S, T = map(int, input().split())
    W = 0
    cnt = 0
    for _ in range(N):
        a = int(input())
        W += a

        if S <= W <= T:
            cnt += 1

    return cnt


if __name__ == '__main__':
    print(main())
