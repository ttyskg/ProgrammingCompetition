import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    X = str(input().strip())
    AE = ['A', 'B', 'C', 'D', 'E']
    return AE.index(X) + 1


if __name__ == '__main__':
    print(main())
