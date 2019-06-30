import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    d = defaultdict(lambda: 0)
    S = str(input().strip())
    for s in S:
        d[s] += 1

    if len(d.keys()) != 2:
        return 'No'

    for k, v in d.items():
        if v != 2:
            return 'No'

    return 'Yes'


if __name__ == '__main__':
    print(main())
