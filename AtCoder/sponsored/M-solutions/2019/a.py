import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    return 180 * (N - 2)

if __name__ == '__main__':
    print(main())
