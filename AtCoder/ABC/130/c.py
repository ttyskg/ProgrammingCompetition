import sys

def main():
    input = sys.stdin.readline
    W, H, x, y = map(int, input().split())
    area = W * H / 2
    way = int(2*x == W and 2*y == H)
    print('{} {}'.format(area, way))

if __name__ == '__main__':
    main()
