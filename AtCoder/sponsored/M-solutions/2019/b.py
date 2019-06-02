import sys

def main():
    input = sys.stdin.readline
    S = [1 for c in input().strip() if c == 'x']
    if sum(S) >= 8:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    print(main())
