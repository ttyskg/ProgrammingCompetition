import sys

def main():
    input = sys.stdin.readline
    N, A, B = map(int, input().split())
    pos = 0
    for _ in range(N):
        b, d = map(str, input().strip().split())
        d = int(d)

        if d < A:
            d = A
        elif d > B:
            d = B

        if b == 'East':
            pos += d
        else: # West
            pos -= d

    if pos == 0:
        print(0)
    elif pos > 0:
        print('East', abs(pos))
    else:
        print('West', abs(pos))


if __name__ == '__main__':
    main()
