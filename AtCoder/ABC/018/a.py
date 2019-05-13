import sys

def main():
    input = sys.stdin.readline
    P = [int(input()) for _ in range(3)]
    R = sorted(P, key=lambda x: -x)

    for p in P:
        print(R.index(p) + 1)


if __name__ == '__main__':
    main()
