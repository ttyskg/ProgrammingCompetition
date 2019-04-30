import sys

def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = [0 for _ in range(N)]
    for _ in range(Q):
        l, r, t = map(int, input().split())
        for i in range(l-1, r):
            A[i] = t

    return print(*A, sep='\n')


if __name__ == '__main__':
    main()
