import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N = int(input())
    d = dict()
    for _ in range(N):
        w, h = map(int, input().split())
        
        if w in d:
            d[w] = min(d[w], h)
        else:
            d[w] = h

    W = sorted(list(d.keys()))
    H = [d[w] for w in W]

    q = deque()
    q.append((H[0], 1))
    for i in range(1, len(H)):
        q_ = deque()
        while len(q) > 0:
            h, cnt = q.popleft()

            if h > H[i]:
                q_.append((H[i], cnt+1))
            else:

    dp =[[0 for _ in range(len(H))] for _ in range(len(H))]
    dp[0][0] = (H[0], 1)
    for i in range(1, H):
        for j in range(i):
            dp[i]

    return ans


if __name__ == '__main__':
    print(main())
