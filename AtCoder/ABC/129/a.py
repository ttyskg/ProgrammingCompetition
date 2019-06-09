import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    A = list(map(int, input().split()))
    A.sort()
    return sum(A[:2])


if __name__ == '__main__':
    print(main())
