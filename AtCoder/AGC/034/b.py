import sys

def main():
    input = sys.stdin.readline
    S = input().strip()
    S = S.replace('BC', 'D')

    ans = 0
    cnt = 0
    for c in S:
        if c == 'A':
            cnt += 1
        elif c == 'D':
            ans += cnt
        else:
            cnt = 0

    return ans


if __name__ == '__main__':
    print(main())
