import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    N = int(input())

    is_ok = False
    k = 2
    while 2**k - 1 <= N:
        if 2**k - 1 == N:
            is_ok = True
            break
        k += 1

    if is_ok:
        print('Yes')
        for i in range(1, 2*N):
            print('{} {}'.format(i, i+1))
        exit()

    print('No')
    exit()


if __name__ == '__main__':
    print(main())
