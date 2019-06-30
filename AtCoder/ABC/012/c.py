import sys

def main():
    input = sys.stdin.readline
    N = int(input())

    total = 0
    for i in range(1, 10):
        for j in range(1, 10):
            total += i * j

    diff = total - N
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == diff:
                print('{} x {}'.format(i, j))


if __name__ == '__main__':
    main()
