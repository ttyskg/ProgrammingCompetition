import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    full = 2**N
    dp = [float('inf')] * full
    dp[0] = 0
    for m in range(M):
        a, b = map(int, input().split())
        C = list(map(int, input().split()))
        state = 0
        for c in C:
            state += 2**(c-1)
        
        for i in range(full):
            if dp[i] != float('inf'):
                dp[i|state] = min(dp[i] + a, dp[i|state])
        
    
    if dp[-1] == float('inf'):
        return -1

    return dp[-1]

if __name__ == '__main__':
    print(main())