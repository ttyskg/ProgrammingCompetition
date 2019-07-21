import sys
 
def main():
    input = sys.stdin.readline
    N = int(input())
    A = [0] + list(map(int, input().split()))
 
    M = 0
    ans = []
    B = [0] * (N+1)
    for i in range(N, 0, -1):
        cnt = 0
        for j in range(2*i, N+1, i):
            cnt += B[j]
 
        if A[i] != cnt % 2:
            B[i] += 1
            M += 1
            ans.append(i)
 
    if M == 0:
        print(0)
    else:
        ans = ans[::-1]
        print(M)
        print(' '.join(map(str, ans)))
 
 
if __name__ == '__main__':
    main()
