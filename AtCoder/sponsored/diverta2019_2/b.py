import sys
from itertools import combinations

def main():
    input = sys.stdin.readline
    N = int(input())
    cord = set()
    for _ in range(N):
        x, y = map(int, input().split())
        cord.add((x, y))

    if N <= 2:
        return 1

    ans = 50
    for a in combinations(cord, 2):
        x1, y1 = a[0]
        x2, y2 = a[1]

        p = x2 - x1
        q = y2 - y1

        cnt1 = 0
        cnt2 = 0

        if p == q == 0:
            continue

        A = set()
        B = set()
        for x, y in cord:
            A.add((x-p, y-q))
            B.add((x+p, y+q))

        ans = min(ans, len(A - cord), len(B - cord))

    return ans


if __name__ == '__main__':
    print(main())
