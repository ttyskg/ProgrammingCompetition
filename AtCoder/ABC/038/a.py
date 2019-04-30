import sys

def main():
    input = sys.stdin.readline
    S = str(input().strip())
    if S[-1] == 'T':
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    print(main())
