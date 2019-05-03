import sys

def main():
    input = sys.stdin.readline
    s = str(input().strip())
    k = int(input())

    n = len(s)
    if k == n:
        return 1

    password = set()
    for i in range(n-k+1):
        password.add(s[i:i+k])

    return len(password)


if __name__ == '__main__':
    print(main())
