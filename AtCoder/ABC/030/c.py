import sys
sys.setrecursionlimit(10**5)

def f(A, B, X, Y, i=0, j=0, cnt=0, time=0):
    while i < len(A) and A[i] < time:
        i += 1

    if i >= len(A):
        return cnt

    time = A[i] + X

    while j < len(B) and B[j] < time:
        j += 1

    if j >= len(B):
        return cnt

    cnt += 1
    time = B[j] + Y
    return f(A, B, X, Y, i, j, cnt, time)


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    return f(A, B, X, Y)


if __name__ == '__main__':
    print(main())
