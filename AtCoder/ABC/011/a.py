import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    N = int(input())
    if N+1 <= 12:
        return N+1
    else:
        return (N+1) % 12


if __name__ == '__main__':
    print(main())
