import sys

def main():
    input = sys.stdin.readline
    ans = 0
    for _ in range(3):
        s, e = map(int, input().split())
        ans += s * e // 10

    return ans


if __name__ == '__main__':
    print(main())
