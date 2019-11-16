import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    S = str(input().strip())

    if N % 2 == 1:
        return 'No'
    
    if S[:N//2] == S[N//2:]:
        return 'Yes'

    return 'No'

if __name__ == '__main__':
    print(main())