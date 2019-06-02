import sys

def main():
    input = sys.stdin.readline
    N, A, B, C, D = map(int, input().split())
    S = input().strip()
    S = S[A-1:max(C, D)]

    if '##' in S:
        return 'No'

    if D > C:
        return 'Yes'

    if '...' in S[B-2:D+1]:
        return 'Yes'

    return 'No'


if __name__ == '__main__':
    print(main())
