import sys

def main():
    input = sys.stdin.readline
    S = str(input().strip())[::-1]
    while len(S) > 0:
        if S[0] in ['o', 'k', 'u']:
            S = S[1:]
        elif S[:2] == 'hc':
            S = S[2:]
        else:
            return 'NO'

    return 'YES'


if __name__ == '__main__':
    print(main())
