import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    S = str(input().strip())
    T = str(input().strip())

    if not set(T) <= set(S):
        return -1

    n = len(S)
    d = defaultdict(list)
    for i, s in enumerate(S, start=1):
        d[s].append(i)

    cnt = 0
    pos = 0
    for t in T:
        if pos >= d[t][-1]:
            cnt += 1
            pos = d[t][0]
        else:
            left = 0
            right = len(d[t])
            while left < right:
                mid = (left + right) // 2
                np = d[t][mid]
                if np <= pos:
                    left = mid + 1
                else:
                    right = mid
            pos = d[t][left]

    return n * cnt + pos


if __name__ == '__main__':
    print(main())
