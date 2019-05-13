import sys
input = sys.stdin.readline

def ask(a, b):
    print("? {0} {1}".format(a, b))
    sys.stdout.flush()
    dist = int(input())

    return dist


def main():
    farthest_node = 0
    farthest_dist = 0
    
    N = int(input())
    for i in range(2, N+1):
        dist = ask(1, i)

        if farthest_dist < dist:
            farthest_dist = dist
            farthest_node = i

    for i in range(2, N+1):
        if i == farthest_node:
            continue

        dist = ask(farthest_node, i)
        farthest_dist = max(farthest_dist, dist)

    print('! {}'.format(farthest_dist))
    sys.stdout.flush()


if __name__ == '__main__':
    main()
