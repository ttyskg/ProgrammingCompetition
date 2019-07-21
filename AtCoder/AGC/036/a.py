import sys

def main():
    input = sys.stdin.readline
    S = int(input())

    x1 = 0
    y1 = 0
    x2 = 10**9

    if S % x2 == 0:
        y2 = 0
        x3 = 0
        y3 = S // x2
    else:
        y2 = 1
        y3 = S // 10**9 + 1
        x3 = 10**9 * y3 - S

    print(x1, y1, x2, y2, x3, y3)


if __name__ == '__main__':
    main()
