import sys
from collections import Counter
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    MOD = 998244353
    N = int(input())
    D = list(map(int, input().split()))

    c = Counter(D)

    if D[0] != 0 or c[0] != 1:
        return 0
    
    ans = 1
    m = max(D)
    for i in range(2, m+1):
        ans *= pow(c[i-1], c[i], MOD)
        ans %= MOD

    return ans

if __name__ == '__main__':
    print(main())