import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        ans += max(0, V[i] - C[i])

    return ans


if __name__ == '__main__':
    print(main())
