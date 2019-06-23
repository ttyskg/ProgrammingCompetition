import sys

def main():
    input = sys.stdin.readline
    N, L = map(int, input().split())

    ans = 10**4
    total = 0
    for i in range(N):
        total += L + i
        if abs(L+i) <= abs(ans):
            ans = L + i

    return total - ans


if __name__ == '__main__':
    print(main())
