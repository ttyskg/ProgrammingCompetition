import sys

def gcd(a, b):
    """Euclidean Algorithm"""
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    N, K = map(int, input().split())

    return ans


if __name__ == '__main__':
    print(main())
