import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    S = str(input().strip())
    n = len(S)

    R = [1 if s == 'R' else 0 for s in S]
    L = [1 if s == 'L' else 0 for s in S]

    A = [0] * n
    r0, r1 = 0, 0
    for i, r in enumerate(R):
        if r == 0:
            if i % 2 == 0:
                A[i] += r0
                A[i-1] += r1
            else:
                A[i] += r1
                A[i-1] += r0

            r0 = 0
            r1 = 0
        else:
            if i % 2 == 0:
                r0 += 1
            else:
                r1 += 1

    B = [0] * n
    l0, l1 = 0, 0
    for i, l in enumerate(L[::-1]):
        if l == 0:
            if i % 2 == 0:
                B[i] += l0
                B[i-1] += l1
            else:
                B[i] += l1
                B[i-1] += l0

            l0 = 0
            l1 = 0
        else:
            if i % 2 == 0:
                l0 += 1
            else:
                l1 += 1

    for a, b in zip(A, B[::-1]):
        print(a + b, end=' ')

    print()


if __name__ == '__main__':
    main()
