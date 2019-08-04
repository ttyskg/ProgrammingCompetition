import sys

def main():
    input = sys.stdin.readline
    A, B, C = map(int, input().split())
    return max(C - (A-B), 0)

if __name__ == '__main__':
    print(main())
