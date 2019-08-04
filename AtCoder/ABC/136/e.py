import sys


def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    S = sum(A)
    divs = set()
    for d in range(1, int(S**(0.5) + 1)):
        if S % d != 0:
            continue
        divs.add(d)
        divs.add(S // d)

    ans = 0
    cost = 0
    for d in divs:
        mods = []
        for a in A:
            mods.append(a % d)
        mods.sort()
        total = sum(mods)
        sub = 0
        for i, m in enumerate(mods, start=1):
            sub += m
            add = d*(N-i) - (total - sub)
            if add == sub:
                cost = sub
                break
        if cost <= K:
            ans = max(ans, d)

    return ans


if __name__ == '__main__':
    print(main())
