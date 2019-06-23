import sys

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = 1
    D = 0
    for a in A:
        D += a
        if D > X:
            break
        cnt += 1

    return cnt


if __name__ == '__main__':
    print(main())
