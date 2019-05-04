import sys
from collections import Counter

def main():
    input = sys.stdin.readline
    S = str(input().strip())
    c = Counter(S)
    ans = []
    for alph in ['A', 'B', 'C', 'D', 'E', 'F']:
        ans.append(c[alph])

    return print(*ans)


if __name__ == '__main__':
    main()
