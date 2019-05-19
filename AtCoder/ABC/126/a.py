import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    S = str(input().strip())

    ans = S[:K-1] + S[K-1].lower() + S[K:]
    return ans


if __name__ == '__main__':
    print(main())
