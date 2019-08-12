import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    ans = 0
    d = defaultdict(lambda: 0)
    N = int(input())
    for _ in range(N):
        s = [c for c in str(input().strip())]
        s.sort()
        s = tuple(s)
        if s in d:
            ans += d[s]
        d[s] += 1

    return ans


if __name__ == '__main__':
    print(main())
