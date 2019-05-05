import sys

def main():
    input = sys.stdin.readline
    S = str(input().strip())
    N = int(input()) - 1
    
    i = N // 5
    j = N % 5

    return S[i] + S[j]


if __name__ == '__main__':
    print(main())
