import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = []
    for _ in range(M):
        b, c = map(int, input().split())
        BC.append((b, c))

    BC = sorted(BC, key=lambda x: -x[1])
    n = 0
    for b, c in BC:
        n += b
        A += [c] * b
        
        if n >= N:
            break

    A = sorted(A, key=lambda x: -x)
    return sum(A[:N])


if __name__ == '__main__':
    print(main())
