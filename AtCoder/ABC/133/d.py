import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))

    ans = [0] * N
    sign = -1
    for a in A:
        sign *= -1
        ans[0] += sign * a

    for i in range(1, N):
        ans[i] = A[i-1] * 2 - ans[i-1]

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
