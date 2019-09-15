import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    ans = (N-1) * N // 2

    return ans


if __name__ == '__main__':
    print(main())
