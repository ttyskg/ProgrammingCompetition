import sys


def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    N, M = map(int, input().split())
    supplements = [0] + [int(input()) for _ in range(N)]

    # dp[i] means the number of ways to eat up to the i-th supplements.
    dp = [0] * (N+1)
    dp[0] = 1
    
    # Memorizing the ingested supplements.
    ingested = set()

    p_acc = 0  # Partial accumulation of the dp table: sum(dp[left:right]).
    left = 0
    for right, sup in enumerate(supplements[1:], start=1):
        if sup in ingested:
            while sup in ingested:
                ingested.remove(supplements[left+1])

                p_acc -= dp[left]
                p_acc %= MOD

                left += 1

        
        ingested.add(sup)

        # Update partial accumulation.
        p_acc += dp[right-1]
        p_acc %= MOD

        dp[right] = p_acc

    return dp[N]


if __name__ == '__main__':
    print(main())
