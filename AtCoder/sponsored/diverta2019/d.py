import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    # From the problem statement, the quotient and remainder of N is the
    # the same k when m is the favorite number.
    #   N = k*m + k = k*(m+1)
    # Here, k is the remainder when N is divided by m, so k < m.
    ans = 0
    for k in range(1, int(N**0.5)+1):
        if N % k == 0:
            m = N // k - 1
            if k >= m:
                break
            ans += m

    return ans


if __name__ == '__main__':
    print(main())
