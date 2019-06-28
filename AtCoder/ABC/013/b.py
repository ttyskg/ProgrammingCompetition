import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    a = int(input())
    b = int(input())

    a, b = min(a, b), max(a, b)
    return min(a + 10 - b, b - a)


if __name__ == '__main__':
    print(main())
