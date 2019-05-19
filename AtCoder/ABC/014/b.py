import sys

def main():
    input = sys.stdin.readline
    n, X = map(int, input().split())
    A = list(map(int, input().split()))[::-1]

    ans = 0
    for i, a in enumerate(A):
        if X & 2**(n-1-i):
            ans += a

    return ans


if __name__ == '__main__':
    print(main())
