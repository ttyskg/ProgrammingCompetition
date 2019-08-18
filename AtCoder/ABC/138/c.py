import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    N = int(input())
    V = list(map(int, input().split()))
    V.sort()
    ans = V[0]
    for i in range(1, N):
        ans = (ans + V[i]) / 2

    return ans


if __name__ == '__main__':
    print(main())
