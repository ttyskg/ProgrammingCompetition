import sys
from itertools import combinations, product


def calc_points(B, C, p):
    s, t = 0, 0
    for i in range(2):
        for j in range(3):
            b = B[i][j]
            if ((i, j) in p and (i+1, j) in p) or ((i, j) not in p and (i+1, j) not in p):
                s += b
            else:
                t += b

    for i in range(3):
        for j in range(2):
            c = C[i][j]
            if ((i, j) in p and (i, j+1) in p) or ((i, j) not in p and (i, j+1) not in p):
                s += c
            else:
                t += c

    return s, t, s+t

def main():
    input = sys.stdin.readline
    B = [list(map(int, input().split())) for _ in range(2)]
    C = [list(map(int, input().split())) for _ in range(3)]

    P = list(product(range(3), repeat=2))
    A = []
    for p in combinations(P, 5):
        s, t, u = calc_points(B, C, p)
        A.append((s, t, u))

    A = sorted(A, key=lambda x: -x[1])
    print(A)



if __name__ == '__main__':
    print(main())
