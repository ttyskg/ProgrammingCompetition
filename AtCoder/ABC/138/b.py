import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for a in A:
        ans += 1/a

    return 1/ans


if __name__ == '__main__':
    print(main())
