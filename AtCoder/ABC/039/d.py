import sys


def is_ori(A, a, b):
    col = []
    for i in range(3):
        for j in range(3):
            col.append(A[a+i-1][b+j-1])

    return all([c == '#' for c in col])


def main():
    input = sys.stdin.readline
    H, W = map(int, input().split())
    A = [0 for _ in range(H+2)]
    A[0] = '#' * (W+2)
    A[H+1] = '#' * (W+2)
    for i in range(H):
        A[i+1] = '#' + str(input().strip()) + '#'

    ans = [['.' for _ in range(W)] for _ in range(H)]
    cont = set()
    blk = set()
    for i in range(1, H+1):
        for j in range(1, W+1):
            if A[i][j] == '#':
                blk.add((i, j))

                if is_ori(A, i, j):
                    ans[i-1][j-1] = '#'
                    for s in range(3):
                        for t in range(3):
                            cont.add((i-1+s, j-1+t))

    if len(blk - cont) > 0:
            print('impossible')
            return 0

    print('possible')
    for a in ans:
        print(''.join(a))


if __name__ == '__main__':
    main()
