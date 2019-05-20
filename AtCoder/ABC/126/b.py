import sys

def main():
    input = sys.stdin.readline
    S = int(input())

    a = S // 100
    b = S % 100

    if (a > 12 or a == 0) and 0 < b <= 12:
        return 'YYMM'
    elif 0 < a <= 12 and (b > 12 or b == 0):
        return 'MMYY'
    elif 0 < a <= 12 and 0 < b <= 12:
        return 'AMBIGUOUS'
    else:
        return 'NA'


if __name__ == '__main__':
    print(main())
