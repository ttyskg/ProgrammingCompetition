import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    l = 0
    for i in range(1, N):
        if A[i] <= A[i-1]:
            n = i - l
            ans += n * (n+1) // 2 - n
            l = i

    n = N - l
    ans += n * (n+1) // 2 - n
    ans += N

    return ans


if __name__ == '__main__':
    print(main())
