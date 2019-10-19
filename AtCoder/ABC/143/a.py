import sys

def main():
    input = sys.stdin.readline
    A, B = map(int, input().split())

    return max(0, A - 2 * B)

if __name__ == '__main__':
    print(main())