import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    L, A, B, M = map(int, input().split())

    S = A + B * (L - 1)
    a = [300000000, 7000000, 110000, 1500, 19]
    for n in a:
        print(n % M)

    return 0


if __name__ == '__main__':
    print(main())
