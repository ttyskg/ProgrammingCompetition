import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    N = int(input())

    h = N // 3600
    N %= 3600
    m = N // 60
    N %= 60

    print("{0:02d}:{1:02d}:{2:02d}".format(h, m, N))


if __name__ == '__main__':
    main()
