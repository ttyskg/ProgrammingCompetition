import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    a, b = map(int, input().split())
    K = int(input())
    P = list(map(int, input().split()))

    P = list(set(P))
    if a in P or b in P or len(P) < K:
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':
    print(main())
