import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N = int(input())
    NG = []
    for _ in range(3):
        NG.append(int(input()))
    NG.sort()

    if N in NG:
        return 'NO'

    safe = [True] * (N+1)
    for ng in NG:
        if ng > N:
            continue
        safe[ng] = False

    cnt = 0
    q = deque()
    q.append(0)
    while len(q) > 0 and cnt <= 100:
        q_ = deque()
        while len(q):
            n = q.pop()

            if n == N:
                return 'YES'

            if n+1 <= N and safe[n+1]:
                q_.append(n+1)
                safe[n+1] = False

            if n+2 <= N and safe[n+2]:
                q_.append(n+2)
                safe[n+2] = False

            if n+3 <= N and safe[n+3]:
                q_.append(n+3)
                safe[n+3] = False

        q = q_
        cnt += 1

    return 'NO'


if __name__ == '__main__':
    print(main())
