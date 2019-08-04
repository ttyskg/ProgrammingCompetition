import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if 1 <= i < 10 or 100 <= i < 1000 or 10000 <= i < 100000:
            ans += 1

    return ans


if __name__ == '__main__':
    print(main())
