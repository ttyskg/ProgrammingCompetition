import sys

def main():
    input = sys.stdin.readline
    S = [str(c) for c in input().strip().split('+')]

    cnt = 0
    for c in S:
        if len(c) == 1:
            if c != '0':
                cnt += 1
        else:
            s = [str(a) for a in c.split('*')]
            if '0' not in s:
                cnt += 1

    return cnt


if __name__ == '__main__':
    print(main())
