import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    n = n % 12

    m_dig = 6 * m
    n_dig = 30 * n + 0.5 * m

    dig = max(n_dig, m_dig) - min(n_dig, m_dig)
    if dig > 180:
        return 360 - dig
    else:
        return dig


if __name__ == '__main__':
    print(main())
