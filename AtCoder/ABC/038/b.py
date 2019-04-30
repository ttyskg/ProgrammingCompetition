import sys

def main():
    input = sys.stdin.readline
    H1, W1 = map(int, input().split())
    H2, W2 = map(int, input().split())

    if H1 == H2 or H1 == W2 or W1 == H2 or W1 == W2:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    print(main())
