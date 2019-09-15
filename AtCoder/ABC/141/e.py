import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    N = int(input())
    S = str(input().strip())

    ans = 0
    for i in range(N):
        for j in range(ans, N-i):
            if len(S[i:i+j]) > len(S[i+j:]):
                break

            if S[i:i+j] in S[i+j:]:
                ans = j


    return ans


if __name__ == '__main__':
    print(main())
