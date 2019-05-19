import sys

def main():
    input = sys.stdin.readline
    S = str(input().strip())

    a = int(S[:2])
    b = int(S[2:])

    if (a > 12 and 0 < b <= 12) or (a == 0 and 0 < b <= 12):
        return 'YYMM'
    elif (0 < a <= 12 and b > 12) or (0 < a <= 12 and b == 0):
        return 'MMYY'
    elif 0 < a <= 12 and 0 < b <= 12:
        return 'AMBIGUOUS'
    else:
        return 'NA'


if __name__ == '__main__':
    print(main())
