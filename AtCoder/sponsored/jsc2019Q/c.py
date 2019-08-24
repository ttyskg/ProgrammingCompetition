import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    N = int(input())
    S = [0 if c == 'W' else 1 for c in str(input().strip())]

    return S


if __name__ == '__main__':
    print(main())
