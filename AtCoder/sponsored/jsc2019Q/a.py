import sys

def main():
    input = sys.stdin.readline
    M, D = map(int, input().split())
    cnt = 0
    for m in range(1, M+1):
        for d in range(1, D+1):
            d1 = d % 10
            d10 = d // 10
            if min(d1, d10) < 2:
                continue
            if d1 * d10 == m:
                cnt += 1

    return cnt


if __name__ == '__main__':
    print(main())
