import sys

def main():
    input = sys.stdin.readline
    S = str(input().strip())
    T = int(input())

    x, y = 0, 0
    cnt = 0
    for s in S:
        if s == 'L':
            x -= 1

        elif s == 'R':
            x += 1

        elif s == 'U':
            y += 1

        elif s == 'D':
            y -= 1

        else:
            cnt += 1

    dist = abs(x) + abs(y)

    if T == 1:
        return dist + cnt
    else:
        if cnt <= dist:
            return dist - cnt
        else:
            return (cnt - dist) % 2


if __name__ == '__main__':
    print(main())
