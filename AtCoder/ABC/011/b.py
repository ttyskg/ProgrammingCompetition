import sys

def main():
    input = sys.stdin.readline
    S = str(input().strip())
    U = S[0].upper()
    L = S[1:].lower()

    return U + L


if __name__ == '__main__':
    print(main())
