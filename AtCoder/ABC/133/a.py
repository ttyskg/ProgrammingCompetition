import sys

def main():
    input = sys.stdin.readline
    N, A, B = map(int, input().split())
    return min(A*N, B)


if __name__ == '__main__':
    print(main())
