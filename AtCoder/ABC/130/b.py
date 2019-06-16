import sys

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = 0
    D = 0
    for a in A:
        D += a
        cnt += 1
        if D > X:
            cnt -= 1
            break

    return cnt+1


if __name__ == '__main__':
    print(main())
