import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    D = list(map(int, input().split()))
    D.sort()

    left, right = D[N//2 - 1], D[N//2]
    return right - left


if __name__ == '__main__':
    print(main())
