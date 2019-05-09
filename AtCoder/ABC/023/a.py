import sys

def main():
    input = sys.stdin.readline
    X = int(input())
    ans = 0
    while X > 0:
        ans += X % 10
        X //= 10

    return ans


if __name__ == '__main__':
    print(main())
