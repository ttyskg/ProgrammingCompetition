import sys
sys.setrecursionlimit(10**6)


def f(x, y):
    res = ''
    if x > 0:
        res += 'p'
    elif y < 0:
        res += 'n'
    else:
        res += '0'

    if y > 0:
        res += 'p'
    elif y < 0:
        res += 'n'
    else:
        res += '0'

    return res


def main():
    input = sys.stdin.readline
    N = int(input())
    P = set()
    P.add((0, 0))
    for _ in range(N):
        x, y = map(int, input().split())
        in_ = f(x, y)

        P_ = set()
        for p in P:
            xp = p[0]
            yp = p[1]
            out_ = f(xp, yp)

            if in_ == out_:
                P_.add((xp + x, yp + y))
            elif in_[0] != out_[0] and in_[1] != out_[1]:
                P_.add((xp, yp))
            elif in_[0] == '0' and in_[1] == '0':
                P_.add((xp, yp))
                P_.add((x, y))
            else:
                P_.add((xp, yp))
                P_.add((xp + x, yp + y))

        P = P_

    print(P)
    ans = 0
    for p in P:
        ans = max(ans, p[0]**2 + p[1]**2)
  
    return ans**0.5


if __name__ == '__main__':
    print(main())
