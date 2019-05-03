import sys

def main():
    input = sys.stdin.readline
    N, a = map(int, input().split())
    k = int(input())
    B = [int(b) - 1 for b in input().split()]
    a -= 1

    cnt = 0
    route = []
    while cnt < k and B[a] not in route:
        a = B[a]
        cnt += 1
        route.append(a)

    if cnt == k:
        return a + 1

    start = route.index(B[a])
    cycle = route[start:]

    n = len(cycle)
    k -= start

    pos = (k % n) - 1
    a = cycle[pos] + 1
    return a


if __name__ == '__main__':
    print(main())
