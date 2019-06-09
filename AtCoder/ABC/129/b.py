import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    ans = 10**5
    for i in range(1, N):
        s1 = sum(A[:i])
        s2 = sum(A[i:])
        ans = min(ans, abs(s1 - s2))

    return ans


if __name__ == '__main__':
    print(main())
