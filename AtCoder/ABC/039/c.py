import sys
from collections import deque

def main():
    input = sys.stdin.readline
    S = [str(c) for c in input().strip()]

    ans = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Si']
    K = ['W', 'B', 'W', 'B', 'W', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
    k =deque()
    k.extend(K)

    for i in range(7):
        if S[0:12] == list(k):
            return ans[i]

        while True:
            a = k.popleft()
            k.append(a)

            if k[0] == 'W':
                break


if __name__ == '__main__':
    print(main())
