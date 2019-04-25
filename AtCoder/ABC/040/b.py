import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    n = int(N**0.5)

    ans = N
    for i in range(1, n+1):
        a = N - (i * (N//i)) + abs(N//i - i)
        ans = min(ans, a)

    return ans


if __name__ == '__main__':
    print(main())
