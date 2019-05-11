import sys

def main():
    input = sys.stdin.readline
    Q = int(input())

    if Q == 1:
        return 'ABC'
    else:
        return 'chokudai'


if __name__ == '__main__':
    print(main())
