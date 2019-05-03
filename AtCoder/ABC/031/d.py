import sys
from copy import deepcopy
from itertools import product


def split_string(string, num):
    splited_strings = []

    for p in product(range(1, 4), repeat=num):
        if sum(p) != len(string):
            continue

        splited = []
        s = 0
        for e in p:
            splited.append(string[s:s+e])
            s += e

        splited_strings.append(splited)

    return splited_strings


def update_dict(ori, keys, vals):
    d = deepcopy(ori)
    for key, val in zip(keys, vals):
        if key not in d:
            d[key] = val

        elif d[key] != val:
            return None

    return d


def main():
    input = sys.stdin.readline
    K, N = map(int, input().split())
    A = [tuple(map(str, input().strip().split())) for _ in range(N)]

    dicts = [dict()]
    for v, w in A:
        seq = [int(i) for i in v]

        dicts_ = []
        splited_w = split_string(w, len(seq))
        for sw in splited_w:
            for d in dicts:
                ud = update_dict(d, seq, sw)

                if ud is not None:
                    dicts_.append(ud)

        dicts = dicts_

    d = dicts[0]
    for i in range(1, K+1):
        print(d[i])


if __name__ == '__main__':
    main()
