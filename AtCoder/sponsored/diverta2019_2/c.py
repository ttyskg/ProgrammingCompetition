import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    q = deque()
    q.extend(A)
    M = q.pop()
    x = q.popleft()
    operation = []
    while len(q) > 0:
        y = q.pop()
        if y < 0:
            operation.append((M, y))
            M -= y
        else:
            operation.append((x, y))
            x -= y

    operation.append((M, x))
    M -= x

    print(M)
    for x, y in operation:
        print('{} {}'.format(x, y))

if __name__ == '__main__':
    main()
