import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7

    para = []
    for i, s in enumerate(A):
        a = 0
        d = 0
        for j, t in enumerate(A):
            if s > t:
                d += 1
                if i < j:
                    a += 1
        para.append((a, d))

    ans = 0
    if K == 1:
        for a, _ in para:
            ans = (ans + a) % MOD
    else:
        for a, d in para:
            s = K * (2*a + (K-1)*d) // 2
            ans = (ans + s) % MOD

    return ans


if __name__ == '__main__':
    print(main())
