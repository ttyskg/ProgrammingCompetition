import sys
from collections import defaultdict

def f(d, p=1):
    childs = d[p]
    if len(childs) == 0:
        return 1

    pay = []
    for c in childs:
        pay.append(f(d, c))

    return max(pay) + min(pay) + 1


def main():
    input = sys.stdin.readline
    N = int(input())
    d = defaultdict(list)
    for i in range(2, N+1):
        b = int(input())
        d[b].append(i)

    return f(d)


if __name__ == '__main__':
    print(main())
