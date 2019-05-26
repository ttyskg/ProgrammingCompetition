import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    restaurants = []
    for _ in range(N):
        s, p = input().split()
        restaurants.append((s.strip(), int(p)))

    rank = sorted(restaurants, key=lambda x: (x[0], -x[1]))
    for a in rank:
        print(int(restaurants.index(a)) + 1)


if __name__ == '__main__':
    main()
