import sys

def main():
    input = sys.stdin.readline
    A, B, C = map(int, input().split())
    return C // min(A, B)


if __name__ == '__main__':
    print(main())
