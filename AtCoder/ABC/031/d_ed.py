import sys
from collections import deque
from itertools import product


def update_dict(d, keys, string, word_len):
    s = 0
    for key in keys:
        l = word_len[key-1]
        word = string[s:s+l]
        s += l

        if key not in d:
            d[key] = word

        elif d[key] != word:
            return None

    return d


def main():
    input = sys.stdin.readline
    K, N = map(int, input().split())
    A = [tuple(map(str, input().strip().split())) for _ in range(N)]

    q = deque()
    for p in product(range(1,4), repeat=K):
        q.append((p, dict()))

    for v, w in A:
        seq = [int(c) for c in v]

        q_ = deque()
        while len(q) > 0:
            p, d = q.popleft()
            if len(w) != sum(p[i-1] for i in seq):
                continue

            d = update_dict(d, seq, w, p)
            if d is not None:
                q_.append((p, d))

        q = q_

    _, d = q.popleft()
    for i in range(1, K+1):
        print(d[i])


if __name__ == '__main__':
    main()
