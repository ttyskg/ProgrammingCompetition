import sys
from itertools import combinations

def main():
    input = sys.stdin.readline
    A = list(map(int, input().split()))

    C = [sum(c) for c in combinations(A, 3)]
    C = sorted(C, key=lambda x: -x)

    return C[2]


if __name__ == '__main__':
    print(main())
