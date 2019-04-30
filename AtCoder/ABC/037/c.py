import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    K = min(K, N - K + 1)
    ans = 0
    for i in range(N):
        if i < K - 1:
            ans += A[i] * (i + 1)

        elif i > N - K:
            ans += A[i] * ((N - (i+1)) % K + 1)

        else:
            ans += A[i] * K

    return ans


if __name__ == '__main__':
    print(main())
