import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    A = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append((a, b))

    A = sorted(A, key=lambda x: x[1])
    time = 0
    for a, b in A:
        time += a
        if time > b:
            return 'No'

    return 'Yes'


if __name__ == '__main__':
    print(main())
