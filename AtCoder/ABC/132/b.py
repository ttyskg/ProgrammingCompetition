import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    P = list(map(int, input().split()))

    cnt = 0
    for i in range(1, N-1):
        p = P[i]
        if min(P[i-1:i+2]) < p < max(P[i-1:i+2]):
            cnt += 1

    return cnt


if __name__ == '__main__':
    print(main())
