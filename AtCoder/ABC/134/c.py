import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    A = []
    for _ in range(N):
        a = int(input())
        A.append(a)

    B = sorted(A, key=lambda x: -x)
    for a in A:
        if a == B[0]:
            print(B[1])
        else:
            print(B[0])


if __name__ == '__main__':
    main()
