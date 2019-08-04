import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    N = int(input())
    H = list(map(int, input().split()))
    c = 0
    for h in H:
        if h < c:
            return 'No'
        c = max(c, h-1)

    return 'Yes'


if __name__ == '__main__':
    print(main())
