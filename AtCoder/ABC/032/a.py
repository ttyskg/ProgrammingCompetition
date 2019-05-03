import sys

def gcd(a, b):
    """Euclidean Algorithm"""
    while b != 0:
        a, b = b, a % b
    return a

def main():
    input = sys.stdin.readline
    a = int(input())
    b = int(input())
    n = int(input())

    lcm = a * b // gcd(a, b)
    return lcm * ((n + lcm -1) // lcm)


if __name__ == '__main__':
    print(main())
