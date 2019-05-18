import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    A = [a for a in map(int, input().split()) if a > 0]

    n = len(A)

    return (sum(A) + n - 1) // n


if __name__ == '__main__':
    print(main())
