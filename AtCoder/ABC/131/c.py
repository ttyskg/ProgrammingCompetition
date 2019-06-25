import sys

def gcd(a, b):
    """Euclidean Algorithm"""
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def main():
    input = sys.stdin.readline
    A, B, C, D = map(int, input().split())
    E = lcm(C, D)

    total = B - (A-1)
    mul_c = B // C - (A-1) // C
    mul_d = B // D - (A-1) // D
    mul_e = B // E - (A-1) // E
    return total - (mul_c + mul_d - mul_e)


if __name__ == '__main__':
    print(main())
