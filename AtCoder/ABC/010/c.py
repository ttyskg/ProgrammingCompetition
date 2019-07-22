import sys

def main():
    input = sys.stdin.readline
    xa, ya, xb, yb, T, V = map(int, input().split())
    n = int(input())
    nearest = 10**6
    for _ in range(n):
        x, y = map(int, input().split())
        moving_distance = ((x - xa)**2 + (y - ya)**2)**(0.5) +\
                          ((x - xb)**2 + (y - yb)**2)**(0.5)
        nearest = min(nearest, moving_distance)

    if nearest <= T * V:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    print(main())
