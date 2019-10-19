import sys
from itertools import combinations

def main():
    input = sys.stdin.readline
    N = int(input())
    d = list(map(int, input().split()))

    ans = 0
    for a, b in combinations(d, 2):
        ans += a * b

    return ans

if __name__ == '__main__':
    print(main())