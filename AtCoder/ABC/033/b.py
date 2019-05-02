import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    lt = ''
    lp = 0
    total = 0
    for _ in range(N):
        s, p = map(str, input().split())
        p = int(p)

        total += p
        if p > lp:
            lt = s
            lp = p

    if lp > total / 2:
        return lt
    else:
        return 'atcoder'


if __name__ == '__main__':
    print(main())
