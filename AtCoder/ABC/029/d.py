import sys

def main():
    input = sys.stdin.readline
    N = int(input())

    ans = 0
    d = 1
    while d < 10:
        ans += N // 10**d * 10**(d-1)
        
        mod = N % 10**d
        if mod >= 10**(d-1):
            ans += min(10**(d-1), mod - 10**(d-1) + 1)

        d += 1

    return int(ans)


if __name__ == '__main__':
    print(main())
