import sys

def main():
    input = sys.stdin.readline
    A, D = map(int, input().split())

    a = (A + 1) * D
    d = A * (D + 1)
    if a >= d:
        return a
    else:
        return d


if __name__ == '__main__':
    print(main())
