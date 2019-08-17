import sys
from collections import deque
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    S = deque([s for s in str(input().strip())])
    cnt = 0
    p = ''
    t = ''
    while len(S) > 0:
        t += S.popleft()
        if p != t:
            cnt += 1
            p = t
            t = ''

    return cnt


if __name__ == '__main__':
    print(main())
