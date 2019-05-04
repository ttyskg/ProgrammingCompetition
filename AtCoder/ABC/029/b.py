import sys

def main():
    input = sys.stdin.readline
    cnt = 0
    for _ in range(12):
        S = str(input().strip())
        if 'r' in S:
            cnt += 1

    return cnt


if __name__ == '__main__':
    print(main())
