import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())

    # Case 1: all numbers are differenct.
    # In this case, one number must be K.
    c1 = (K - 1) * (N - K) * 6

    # Case 2: two numbers are K.
    # In this case, the rest number can be anything excepting K.
    c2 = (N - 1) * 3

    # Case 3: all munbers are K.
    c3 = 1

    return (c1 + c2 + c3) / N**3


if __name__ == '__main__':
    print(main())
