import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())

    ans = 0
    for i in range(1, N+1):
        if i >= K:
            ans += 1 / N
        else:
            cnt = 1
            while i * 2**cnt < K:
                cnt += 1

            ans += 1 / N * (0.5)**cnt

    return ans


if __name__ == '__main__':
    print(main())
