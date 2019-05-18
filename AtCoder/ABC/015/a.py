import sys

def main():
    input = sys.stdin.readline
    A = str(input().strip())
    B = str(input().strip())

    if len(A) > len(B):
        return A
    else:
        return B


if __name__ == '__main__':
    print(main())
