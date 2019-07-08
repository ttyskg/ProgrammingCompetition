import sys

def main():
    input = sys.stdin.readline
    L, R = map(int, input().split())
    R = min(R, L + 2019)

    ans = 2019
    for i in range(L, R):
        for j in range(i+1, R+1):
            ans = min(ans, (i*j)%2019)
            if ans == 0:
                return 0

    return ans


if __name__ == '__main__':
    print(main())
