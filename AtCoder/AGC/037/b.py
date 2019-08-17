import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    N = int(input())
    S = str(input().strip())
    MOD = 998244353

    #state = (_, r, g, b, rg, gb, br)
    def f(i, ans, state):
        if i > 3*N-1:
            return ans
        if min(state) < 0:
            return 0

        no_ball, r, g, b, rg, gb, br = state
        if S[i] == 'R':
            if gb > 0:
                ans = (ans * gb) % MOD
                return f(i+1, ans, [no_ball, r, g, b, rg, gb-1, br])
            elif g > 0 or b > 0:
                ans = ans * (g + b) % MOD
                s1 = [no_ball, r, g-1, b, rg+1, gb, br]
                s2 = [no_ball, r, g, b-1, rg, gb, br+1]
                return (f(i+1, ans, s1) + f(i+1, ans, s2)) % MOD
            else:
                ans = (ans * no_ball) % MOD
                return f(i+1, ans, [no_ball-1, r+1, g, b, rg, gb, br])

        elif S[i] == 'G':
            if br > 0:
                ans = (ans * br) % MOD
                return f(i+1, ans, [no_ball, r, g, b, rg, gb, br-1])
            elif r > 0 or b > 0:
                ans = ans * (r + b) % MOD
                s1 = [no_ball, r-1, g, b, rg+1, gb, br]
                s2 = [no_ball, r, g, b-1, rg, gb+1, br]
                return (f(i+1, ans, s1) + f(i+1, ans, s2)) % MOD
            else:
                ans = (ans * no_ball) % MOD
                return f(i+1, ans, [no_ball-1, r, g+1, b, rg, gb, br])

        else: #S[i] == 'B':
            if rg > 0:
                ans = (ans * rg) % MOD
                return f(i+1, ans, [no_ball, r, g, b, rg-1, gb, br])
            elif r > 0 or g > 0:
                ans = ans * (r + g) % MOD
                s1 = [no_ball, r-1, g, b, rg, gb, br+1]
                s2 = [no_ball, r, g-1, b, rg, gb+1, br]
                return (f(i+1, ans, s1) + f(i+1, ans, s2)) % MOD
            else:
                ans = (ans * no_ball) % MOD
                return f(i+1, ans, [no_ball-1, r, g, b+1, rg, gb, br])

    return f(0, 1, [N, 0, 0, 0, 0, 0, 0]) % MOD


if __name__ == '__main__':
    print(main())
