import sys

def main():
    input = sys.stdin.readline
    A, B, C = map(int, input().split())

    if A + B == A - B == C:
        return '?'
    elif A + B == C:
        return '+'
    elif A - B == C:
        return '-'
    else:
        return '!'


if __name__ == '__main__':
    print(main())
