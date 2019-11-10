import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    ans = N // 2
    if ans * 2 == N:
        ans -= 1

    return ans

if __name__ == '__main__':
    print(main())