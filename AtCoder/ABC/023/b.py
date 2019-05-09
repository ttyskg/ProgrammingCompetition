import sys

def make_accessary(n):
    s = 'b'
    i = 0
    while len(s) < n:
        i += 1
        if i % 3 == 1:
            s = 'a' + s + 'c'
        elif i % 3 == 2:
            s = 'c' + s + 'a'
        else:
            s = 'b' + s + 'b'

    return s


def main():
    input = sys.stdin.readline
    N = int(input())
    S = str(input().strip())

    if N % 2 == 0:
        return -1

    correct = make_accessary(N)
    if S == correct:
        return (N-1) // 2
    else:
        return -1


if __name__ == '__main__':
    print(main())
