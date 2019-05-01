import sys

def main():
    input = sys.stdin.readline
    W, H = map(int, input().split())

    if H * 4 == W * 3:
        return '4:3'
    else:
        return '16:9'


if __name__ == '__main__':
    print(main())
