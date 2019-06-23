import sys

def main():
    input = sys.stdin.readline
    W, H, x, y = map(int, input().split())
    area = W * H / 2
    is_centroid = int(2*x == W and 2*y == H)
    print('{} {}'.format(area, is_centroid))

if __name__ == '__main__':
    main()
