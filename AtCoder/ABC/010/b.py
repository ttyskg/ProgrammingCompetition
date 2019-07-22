import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))

    cnt = 0
    for a in A:
        if a % 6 == 0:
            cnt += 3
        elif a % 3 == 2 and a % 2 == 1:
            cnt += 2
        elif a % 3 == 2:
            cnt += 1
        elif a % 2 == 0:
            cnt += 1

    return cnt


if __name__ == '__main__':
    print(main())
