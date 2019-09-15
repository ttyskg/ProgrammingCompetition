import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    H = list(map(int, input().split()))

    A = [0] * N
    ch = 0
    for i, h in enumerate(H):
        if ch >= h:
            A[i] = A[i-1] + 1
            ch = h
        else:
            ch = h

    return max(A)


if __name__ == '__main__':
    print(main())
