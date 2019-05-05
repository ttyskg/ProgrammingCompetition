import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    S = str(input().strip())
    p, n = 0, 0
    for s in S:
        if s == '+':
            p += 1
        if s == '-':
            n += 1

    A = []
    for s in S:
        if s == 'M':
            A.append(p-n)
        elif s == '+':
            p -= 1
        else: # s == '-'
            n -= 1

    A.sort()
    N = len(A)
    left_move = A[:N//2]
    right_move = A[N//2:]

    return sum(right_move) - sum(left_move)

if __name__ == '__main__':
    print(main())
