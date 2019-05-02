import sys

def main():
    input = sys.stdin.readline
    x, y = map(int, input().split())
    if y > x:
        return 'Better'
    else:
        return 'Worse'


if __name__ == '__main__':
    print(main())
