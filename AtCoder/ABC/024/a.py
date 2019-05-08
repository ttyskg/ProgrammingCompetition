import sys

def main():
    input = sys.stdin.readline
    A, B, C, K = map(int, input().split())
    S, T = map(int, input().split())

    ans = A * S + B * T
    if S + T >= K:
        ans -= C * (S + T)

    return ans


if __name__ == '__main__':
    print(main())
