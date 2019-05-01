import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    rank = set()
    A = []
    for _ in range(N):
        a = int(input())
        A.append(a)
        rank.add(a)

    rank = sorted(list(rank))
    d = dict()
    for i in range(len(rank)):
        d[rank[i]] = i

    for a in A:
        print(d[a])


if __name__ == '__main__':
    main()
