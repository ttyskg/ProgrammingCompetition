import sys

def main():
    input = sys.stdin.readline
    S = str(input().strip())
    ans = ''
    c = S[0]
    S += '*'
    cnt = 0
    for s in S:
        if c == s:
            cnt += 1
        else:
            ans += c + str(cnt)
            c = s
            cnt = 1

    return ans


if __name__ == '__main__':
    print(main())
