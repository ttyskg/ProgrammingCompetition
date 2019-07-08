import sys

def main():
    input = sys.stdin.readline
    N, D = map(int, input().split())
    X = []
    for _ in range(N):
        A = tuple(map(int, input().split()))
        X.append(A)

    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            s = 0
            for d in range(D):
                s += (X[i][d] - X[j][d])**2

            t = int(s**(0.5))
            if s == t**2:
                ans += 1

    return ans


if __name__ == '__main__':
    print(main())
