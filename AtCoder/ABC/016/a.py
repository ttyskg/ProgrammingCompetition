import sys

def main():
    input = sys.stdin.readline
    M, D = map(int, input().split())

    if M % D == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    print(main())
