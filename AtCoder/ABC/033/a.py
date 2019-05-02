import sys

def main():
    input = sys.stdin.readline
    digits = [int(n) for n in input().strip()]
    if len(set(digits)) == 1:
        return 'SAME'
    else:
        return 'DIFFERENT'


if __name__ == '__main__':
    print(main())
