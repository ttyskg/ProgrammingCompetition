import sys

def main():
    input = sys.stdin.readline
    S = str(input().strip())
    T = str(input().strip())

    cnt = 0
    for (s, t) in zip(S, T):
        if s == t:
            cnt += 1

    return cnt


if __name__ == '__main__':
    print(main())
