import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    S = [[str(c) for c in input().strip()] for _ in range(N)]

    ans = ['' for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ans[i] += S[N-1-j][i]

    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
