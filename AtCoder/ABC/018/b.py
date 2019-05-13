import sys

def main():
    input = sys.stdin.readline
    S = str(input().strip())
    N = int(input())
    for _ in range(N):
        left, right = map(int, input().split())
        left -= 1
        right -= 1
        S = S[:left] + S[left:right+1][::-1] + S[right+1:]

    return S


if __name__ == '__main__':
    print(main())
