import sys

def main():
    input = sys.stdin.readline
    A, B = map(int, input().split())
    cnt = 0
    tap = 1
    while tap < B:
        tap += A - 1
        cnt += 1

    return cnt


if __name__ == '__main__':
    print(main())
