import sys

def main():
    input = sys.stdin.readline
    A, B, C, D = map(int, input().split())
    if B / A == D / C:
        return 'DRAW'
    elif B / A > D / C:
        return 'TAKAHASHI'
    else:
        return 'AOKI'


if __name__ == '__main__':
    print(main())
