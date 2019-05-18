import sys
from itertools import product

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]

    for answers in product(*T):
        output = 0
        for n in answers:
            output ^= n

        if output == 0:
            return 'Found'

    return 'Nothing'


if __name__ == '__main__':
    print(main())
