import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    S = str(input().strip())

    cnt = 0
    color = '_'
    for s in S:
        if s == color:
            continue
        cnt += 1
        color = s

    return cnt

if __name__ == '__main__':
    print(main())