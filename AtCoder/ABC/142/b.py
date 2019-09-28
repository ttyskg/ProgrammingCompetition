import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = 0
    for h in A:
        if h >= K:
            cnt += 1

    return cnt

if __name__ == '__main__':
    print(main())