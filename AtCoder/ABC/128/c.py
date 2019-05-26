import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    bulbs = []
    for _ in range(M):
        b = tuple(map(int, input().split()))
        bulbs.append(b[1:])

    P = list(map(int, input().split()))

    ans = 0
    for switch in range(2**N):
        check = [0] * M
        for i, bulb in enumerate(bulbs):
            cnt = 0
            for b in bulb:
                if switch >> (b - 1) & 1:
                    cnt += 1

            if cnt % 2 == P[i]:
                check[i] = True
            else:
                check[i] = False

        if all(check):
            ans += 1

    return ans


if __name__ == '__main__':
    print(main())
