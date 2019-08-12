import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    K, X = map(int, input().split())
    ans = []
    start = X - K + 1
    end = X + K
    for i in range(start, end):
        ans.append(i)

    return ' '.join(map(str, ans))


if __name__ == '__main__':
    print(main())
